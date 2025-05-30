"""Get terms from geonames."""

from __future__ import annotations

import logging
from collections.abc import Iterable, Mapping

import pandas as pd
from pystow.utils import read_zipfile_csv
from tqdm import tqdm

from pyobo import Obo, Term
from pyobo.sources.geonames.utils import (
    ADMIN1_URL,
    ADMIN2_URL,
    ADMIN_1,
    ADMIN_2,
    CITIES_URL,
    CITY,
    CODE_TYPEDEF,
    COUNTRIES_URL,
    FEATURE_TERM,
    NATION,
    P_CATEGORY,
    PREFIX,
    PREFIX_FEATURE,
    SYNONYMS_DF_COLUMNS,
    SYNONYMS_URL,
    get_feature_terms,
)
from pyobo.struct import Reference, has_part, part_of
from pyobo.utils.path import ensure_df, ensure_path

__all__ = ["GeonamesGetter"]

logger = logging.getLogger(__name__)


class GeonamesGetter(Obo):
    """An ontology representation of GeoNames."""

    ontology = PREFIX
    dynamic_version = True
    typedefs = [part_of, CODE_TYPEDEF, has_part]

    def iter_terms(self, force: bool = False) -> Iterable[Term]:
        """Iterate over terms in the ontology."""
        return get_terms(force=force)


def get_terms(*, force: bool = False) -> Iterable[Term]:
    """Get terms."""
    yield Term(reference=NATION)
    yield Term(reference=ADMIN_1).append_relationship(part_of, NATION)
    yield Term(reference=ADMIN_2).append_relationship(part_of, ADMIN_1)
    yield Term(reference=CITY)

    # since the output here is only cities, we can slice this down
    for term in get_feature_terms(force=force):
        if term.identifier.startswith("P.") or term.pair == P_CATEGORY.pair or term == FEATURE_TERM:
            yield term

    code_to_country = get_code_to_country(force=force)
    yield from code_to_country.values()

    code_to_admin1 = get_code_to_admin1(code_to_country, force=force)
    yield from code_to_admin1.values()

    code_to_admin2 = get_code_to_admin2(
        code_to_country=code_to_country, code_to_admin1=code_to_admin1, force=force
    )
    yield from code_to_admin2.values()

    id_to_term = get_cities(
        code_to_country=code_to_country,
        code_to_admin1=code_to_admin1,
        code_to_admin2=code_to_admin2,
        force=force,
    )
    yield from list(id_to_term.values())


def get_code_to_country(*, force: bool = False) -> Mapping[str, Term]:
    """Get a mapping from country code to country term."""
    countries_df = ensure_df(
        PREFIX,
        url=COUNTRIES_URL,
        force=force,
        skiprows=49,
        keep_default_na=False,  # NA is a country code
        dtype=str,
    )
    logger.info(f"got {len(countries_df.index):,} countries")
    reorder = ["geonameid", *(c for c in countries_df.columns if c != "geonameid")]
    countries_df = countries_df[reorder]
    code_to_country = {}
    cols = ["geonameid", "Country", "#ISO", "fips", "ISO3"]
    for identifier, name, code, fips, iso3 in countries_df[cols].values:
        if pd.isna(code):
            continue
        term = Term(
            reference=Reference(
                prefix=PREFIX, identifier=identifier, name=name if pd.notna(name) else None
            ),
            type="Instance",
        )
        term.append_parent(NATION)
        term.append_synonym(code)
        if name.startswith("The "):
            term.append_synonym(name.removeprefix("The "))
        if pd.notna(fips):
            term.append_synonym(fips)
        if pd.notna(iso3):
            term.append_synonym(iso3)
        term.annotate_string(CODE_TYPEDEF, code)
        code_to_country[code] = term
    logger.info(f"got {len(code_to_country):,} country records")
    return code_to_country


def get_code_to_admin1(
    code_to_country: Mapping[str, Term], *, force: bool = False
) -> Mapping[str, Term]:
    """Get a mapping from admin1 code to term."""
    admin1_df = ensure_df(
        PREFIX,
        url=ADMIN1_URL,
        header=None,
        names=["code", "name", "asciiname", "geonames_id"],
        dtype=str,
        force=force,
    )
    code_to_admin1 = {}
    for code, name, asciiname, identifier in admin1_df.values:
        if pd.isna(identifier) or pd.isna(code):
            tqdm.write(f"Missing info for  {name} / {asciiname} / {code=} / {identifier=}")
            continue

        term = Term(
            reference=Reference(
                prefix=PREFIX, identifier=identifier, name=name if pd.notna(name) else None
            ),
            type="Instance",
        )
        term.append_parent(ADMIN_1)
        term.annotate_string(CODE_TYPEDEF, code)
        code_to_admin1[code] = term

        country_code = code.split(".")[0]
        country_term = code_to_country[country_code]
        term.append_relationship(part_of, country_term)
    return code_to_admin1


def get_code_to_admin2(
    *, code_to_country: Mapping[str, Term], code_to_admin1: Mapping[str, Term], force: bool = False
) -> Mapping[str, Term]:
    """Get a mapping from admin2 code to term."""
    admin2_df = ensure_df(
        PREFIX,
        url=ADMIN2_URL,
        header=None,
        names=["code", "name", "asciiname", "geonames_id"],
        dtype=str,
        force=force,
    )
    code_to_admin2 = {}
    for identifier, name, code in admin2_df[["geonames_id", "name", "code"]].values:
        if pd.isna(identifier) or pd.isna(code):
            continue
        term = Term(
            reference=Reference(
                prefix=PREFIX, identifier=identifier, name=name if pd.notna(name) else None
            ),
            type="Instance",
        )
        term.append_parent(ADMIN_2)
        term.annotate_string(CODE_TYPEDEF, code)
        code_to_admin2[code] = term
        admin1_code = code.rsplit(".", 1)[0]
        admin1_term = code_to_admin1.get(admin1_code)
        if admin1_term:
            term.append_relationship(part_of, admin1_term)
        else:
            country_code = admin1_code.split(".", 1)[0]
            country_term = code_to_country[country_code]
            term.append_relationship(part_of, country_term)
    return code_to_admin2


def _get_cities_df(force: bool = False) -> pd.DataFrame:
    columns = [
        "geonames_id",
        "name",
        "asciiname",
        "synonyms",
        "latitude",
        "longitude",
        "feature_class",
        "feature_code",
        "country_code",
        "cc2",
        "admin1",
        "admin2",
        "admin3",
        "admin4",
        "population",
        "elevation",
        "dem",
        "timezone",
        "date_modified",
    ]
    path = ensure_path(PREFIX, url=CITIES_URL, force=force)
    cities_df = read_zipfile_csv(
        path=path,
        inner_path="cities15000.txt",
        header=None,
        names=columns,
        dtype=str,
    )
    return cities_df


def _get_synonyms_df(force: bool = False) -> pd.DataFrame:
    """Get the synonyms dataframe."""
    path = ensure_path(PREFIX, url=SYNONYMS_URL, force=force)
    synonyms_df = read_zipfile_csv(
        path=path,
        inner_path="alternateNamesV2.txt",
        header=None,
        names=SYNONYMS_DF_COLUMNS,
        dtype=str,
    )
    return synonyms_df


def get_cities(
    code_to_country,
    code_to_admin1,
    code_to_admin2,
    *,
    minimum_population: int = 100_000,
    force: bool = False,
    include_synonyms: bool = False,
) -> dict[str, Term]:
    """Get a mapping from city code to term."""
    cities_df = _get_cities_df(force=force)
    cities_df = cities_df[cities_df.population.astype(int) > minimum_population]
    cities_df.synonyms = cities_df.synonyms.str.split(",")

    terms = {}
    for term in code_to_country.values():
        terms[term.identifier] = term

    cols = ["geonames_id", "name", "synonyms", "country_code", "admin1", "admin2", "feature_code"]
    for identifier, name, synonyms, country, admin1, admin2, feature_code in cities_df[cols].values:
        terms[identifier] = term = Term(
            reference=Reference(
                prefix=PREFIX, identifier=identifier, name=name if pd.notna(name) else None
            ),
            type="Instance",
        )
        # All cities are under the P branch, but the prefix is omitted for brevity in the TSV
        term.append_parent(Reference(prefix=PREFIX_FEATURE, identifier=f"P.{feature_code}"))
        term.append_parent(CITY)

        if include_synonyms and synonyms and not isinstance(synonyms, float):
            # TODO include language codes
            for synonym in synonyms:
                if pd.notna(synonym):
                    term.append_synonym(synonym)

        if pd.isna(admin1):
            # TODO try to annotate these directly onto countries
            tqdm.write(
                f"[geonames:{identifier}] {name}, a city in {country}, is missing admin 1 code"
            )
            continue

        admin1_full = f"{country}.{admin1}"
        admin1_term = code_to_admin1.get(admin1_full)
        if admin1_term is None:
            logger.info(f"could not find admin1 {admin1_full}")
            continue

        terms[admin1_term.identifier] = admin1_term

        if pd.notna(admin2):
            admin2_full = f"{country}.{admin1}.{admin2}"
            admin2_term = code_to_admin2.get(admin2_full)
            if admin2_term is None or admin1_term is None:
                pass
                # print("could not find admin2", admin2_full)
            else:
                term.append_relationship(part_of, admin2_term)
                terms[admin2_term.identifier] = admin2_term

        else:  # pd.notna(admin1):
            # If there's no admin 2, just annotate directly onto admin 1
            term.append_relationship(part_of, admin1_term)

    return terms


def get_city_to_country() -> dict[str, str]:
    """Get a mapping from city GeoNames to country GeoNames id."""
    rv = {}
    code_to_country = get_code_to_country()
    cities_df = _get_cities_df()
    for city_geonames_id, country_code in cities_df[["geonames_id", "country_code"]].values:
        if pd.isna(city_geonames_id) or pd.isna(country_code):
            continue
        rv[city_geonames_id] = code_to_country[country_code].identifier
    return rv


if __name__ == "__main__":
    GeonamesGetter.cli()
