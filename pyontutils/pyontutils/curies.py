import yaml
from pathlib import Path
from pyontutils.config import auth
from pyontutils.utils_fast import log


def interlex_namespace(user):
    return 'http://uri.interlex.org/' + user

def getCuries(curies_location):
    # FIXME this will 'fail' silently ...
    # probably need to warn?
    try:
        if curies_location is None:
            raise TypeError('curies should always fail over to '
                            '.config/pyontutils/curie_map.yaml '
                            'what have you done!?')

        if not curies_location.exists():
            # windows pip user install madness probably
            log.warning(f'no curies_map.yaml found, searching')
            _node = Path(__file__).parent
            _searching = True
            while _searching:
                if _node.parent == _node:
                    break
                _maybe_share = _node / 'share'
                if _maybe_share.exists():
                    for p in _maybe_share.rglob('**/curie_map.yaml'):
                        curies_location = p
                        log.info(
                            f'curies_map.yaml found at: {p}\n'
                            'if this was slow, or to silenced this message\n'
                            f'copy {p} to ' + str(auth._pathit(
                            '{:user-config-path}/pyontutils/curie_map.yaml'))
                            + '\n')
                        _searching = False
                        break

                _node = _node.parent

        # TODO staleness check
        with open(curies_location, 'rt') as f:
            curie_map = yaml.safe_load(f)

        return curie_map

    except (FileNotFoundError, NotADirectoryError) as e:
        log.exception(e)
        # retrieving stuff over the net is bad
        # but having stale curies seems worse?

        # current options for retrieval
        # github, best, but rate limit problems
        # ontquery CURIE_MAP
        # ../nifstd/scigraph/curie_map.yaml
        # Cypher()
        # strong coupling between the version
        # in this repo at this commit is what
        # causes the issue, github is the best
        # solution, so write once to a known location

        import requests
        if curies_location == Path(auth.get_default('curies')):
            master_blob = 'https://github.com/tgbugs/pyontutils/blob/master/'
            raw_path = 'nifstd/scigraph/curie_map.yaml?raw=true'
            curies_url = master_blob + raw_path
            resp = requests.get(curies_url)
            if resp.ok:
                clp = Path(curies_location)
                if not clp.parent.exists():
                    clp.parent.mkdir()

                with open(clp, 'wt') as f:
                    f.write(resp.text)

                print(f'Wrote {clp} from {curies_url}')
                return getCuries(curies_location)

            else:
                raise requests.ConnectionError(resp.request, resp)
        else:
            raise TypeError(f'{curies_location} does not exist and '
                            f'is not at the default {auth.get("curies")} '
                            'so we will not write to it. You can update it '
                            'manually if you want to keep it at that location.')


def _loadPrefixes():
    curie_map = getCuries(auth.get_path('curies'))
    # holding place for values that are not in the curie map
    full = {
        # interlex predicates  PROVISIONAL
        'ilx.includesTerm': 'http://uri.interlex.org/base/ilx_0770273',
        'ilx.includesTermSet': 'http://uri.interlex.org/base/ilx_0770271',
        'ilx.includeForSPARC': 'http://uri.interlex.org/base/ilx_0738400',
        'ilx.federatesElement': 'http://uri.interlex.org/base/ilx_0381445',
        'ilx.relatedTo': 'http://uri.interlex.org/base/ilx_0112796',
        'ilx.hasRole': 'http://uri.interlex.org/base/ilx_0112784',
        'ilx.partOf': 'http://uri.interlex.org/base/ilx_0112785',
        'ilx.anno.hasConstraint': 'http://uri.interlex.org/base/ilx_0115071',
        'ilx.anno.filterElement': 'http://uri.interlex.org/base/ilx_0381352',
        'ilx.anno.required': 'http://uri.interlex.org/base/ilx_0381353',
        'ilx.anno.condition': 'http://uri.interlex.org/base/ilx_0381354',
        'ilx.anno.size': 'http://uri.interlex.org/base/ilx_0381355',
        'ilx.anno.minValue': 'http://uri.interlex.org/base/ilx_0381356',
        'ilx.anno.maxValue': 'http://uri.interlex.org/base/ilx_0381357',
        'ilx.anno.allowedTypes': 'http://uri.interlex.org/base/ilx_0381358',
        'ilx.anno.allowedValues': 'http://uri.interlex.org/base/ilx_0381359',

        'ilx.anno.hasExactSynonym': 'http://uri.interlex.org/base/ilx_0737161',
        'ilx.anno.hasRelatedSynonym': 'http://uri.interlex.org/base/ilx_0737162',
        'ilx.anno.hasNarrowSynonym': 'http://uri.interlex.org/base/ilx_0737163',
        'ilx.anno.hasBroadSynonym': 'http://uri.interlex.org/base/ilx_0737164',

        'ilx.hasDefinitionSource': 'http://uri.interlex.org/base/ilx_0739292',
        'ilx.anno.hasDefinitionSource': 'http://uri.interlex.org/base/ilx_0777130',

        'ilx.hasDbXref': 'http://uri.interlex.org/base/ilx_0381360',
        'ilx.hasUnit': 'http://uri.interlex.org/base/ilx_0381384',
        'ilx.isAbout': 'http://uri.interlex.org/base/ilx_0381385',  # should probalby map to iao
        'ilx.hasLaterality': 'http://uri.interlex.org/base/ilx_0381387',  # FIXME being treated data property
        'ilx.hasMeasurementType': 'http://uri.interlex.org/base/ilx_0381388',
        'ilx.isMeasureOf': 'http://uri.interlex.org/base/ilx_0381389',

        'NINDS.CDE': interlex_namespace('NINDSCDE/uris/readable/'),
        'ilx.type': 'http://uri.interlex.org/base/readable/type/',

        #'':None,  # safety (now managed directly in the curies file)
        #'EHDAA2':'http://purl.obolibrary.org/obo/EHDAA2_',  # FIXME needs to go in curie map?

        # RO predicates
        'hasRole':'http://purl.obolibrary.org/obo/RO_0000087',
        'inheresIn':'http://purl.obolibrary.org/obo/RO_0000052',
        'bearerOf':'http://purl.obolibrary.org/obo/RO_0000053',
        'participatesIn':'http://purl.obolibrary.org/obo/RO_0000056',
        'hasParticipant':'http://purl.obolibrary.org/obo/RO_0000057',
        'hasInput':'http://purl.obolibrary.org/obo/RO_0002233',
        'hasOutput':'http://purl.obolibrary.org/obo/RO_0002234',
        'adjacentTo':'http://purl.obolibrary.org/obo/RO_0002220',
        'derivesFrom':'http://purl.obolibrary.org/obo/RO_0001000',
        'derivesInto':'http://purl.obolibrary.org/obo/RO_0001001',
        'agentIn':'http://purl.obolibrary.org/obo/RO_0002217',
        'hasAgent':'http://purl.obolibrary.org/obo/RO_0002218',
        'containedIn':'http://purl.obolibrary.org/obo/RO_0001018',
        'contains':'http://purl.obolibrary.org/obo/RO_0001019',
        'locatedIn':'http://purl.obolibrary.org/obo/RO_0001025',
        'locationOf':'http://purl.obolibrary.org/obo/RO_0001015',
        'toward':'http://purl.obolibrary.org/obo/RO_0002503',
        'overlaps':'http://purl.obolibrary.org/obo/RO_0002131',

        'replacedBy':'http://purl.obolibrary.org/obo/IAO_0100001',
        'hasCurStatus':'http://purl.obolibrary.org/obo/IAO_0000114',
        'definition':'http://purl.obolibrary.org/obo/IAO_0000115',
        'editorNote':'http://purl.obolibrary.org/obo/IAO_0000116',
        'termEditor':'http://purl.obolibrary.org/obo/IAO_0000117',
        'altTerm':'http://purl.obolibrary.org/obo/IAO_0000118',
        'defSource':'http://purl.obolibrary.org/obo/IAO_0000119',
        'termsMerged':'http://purl.obolibrary.org/obo/IAO_0000227',
        'obsReason':'http://purl.obolibrary.org/obo/IAO_0000231',
        'curatorNote':'http://purl.obolibrary.org/obo/IAO_0000232',
        'importedFrom':'http://purl.obolibrary.org/obo/IAO_0000412',
        'isAbout':'http://purl.obolibrary.org/obo/IAO_0000136',

        # realizes the proper way to connect a process to a continuant
        'realizedIn':'http://purl.obolibrary.org/obo/BFO_0000054',
        'realizes':'http://purl.obolibrary.org/obo/BFO_0000055',

        'partOf':'http://purl.obolibrary.org/obo/BFO_0000050',
        'hasPart':'http://purl.obolibrary.org/obo/BFO_0000051',
        'memberOf': 'http://purl.obolibrary.org/obo/RO_0002350',
        'hasMember': 'http://purl.obolibrary.org/obo/RO_0002351',
    }

    normal = {
        # for obo files with 'fake' namespaces, http://uri.interlex.org/fakeobo/uris/ eqiv to purl.obolibrary.org/
        'fobo':'http://uri.interlex.org/fakeobo/uris/obo/',

        'hyp':'https://hyp.is/',

        'PROTEGE':'http://protege.stanford.edu/plugins/owl/protege#',
        'TEMP': interlex_namespace('temp/uris/'),
        'TEMPRAW': interlex_namespace('temp/uris/raw/'),
        'TEMPIND': interlex_namespace('temp/uris/phenotype-indicators/'),
        'lex': interlex_namespace('base/lexical/'),
        'npokb': interlex_namespace('npo/uris/neurons/'),
        'tech': interlex_namespace('tgbugs/uris/readable/technique/'),
        'FIXME':'http://FIXME.org/',
        'NIFRAW':'https://raw.githubusercontent.com/SciCrunch/NIF-Ontology/',
        'NIFTTL':'http://ontology.neuinfo.org/NIF/ttl/',
        'NIFBASE':'http://ontology.neuinfo.org/NIF/',  # XXX order should not matter but does?
        'NIFRET':'http://ontology.neuinfo.org/NIF/Retired/NIF-Retired.owl#',
        'NLXWIKI':'http://neurolex.org/wiki/',
        # FIXME a thought: was # intentionally used to increase user privacy? or is this just happenstance?
        'nsu':'http://www.FIXME.org/nsupper#',
        'oboInOwl':'http://www.geneontology.org/formats/oboInOwl#',
        'ro':'http://www.obofoundry.org/ro/ro.owl#',

        # defined by chebi.owl, confusingly chebi#2 -> chebi1 maybe an error?
        # better to keep it consistent in case someone tries to copy and paste
        'chebi1':'http://purl.obolibrary.org/obo/chebi#2',
        'chebi2':'http://purl.obolibrary.org/obo/chebi#',
        'chebi3':'http://purl.obolibrary.org/obo/chebi#3',
        'JAX':'http://jaxmice.jax.org/strain/',
        'PTHR': 'http://www.pantherdb.org/panther/family.do?clsAccession=PTHR',  # FIXME evil just like the SAO issue, why do people put dead prefixes with no sep ;_;
    }
    #extras = {**{k:rdflib.URIRef(v) for k, v in full.items()}, **normal}
    extras = {**full, **normal}
    curie_map.update(extras)
    return curie_map


PREFIXES = _loadPrefixes()


__all__ = sorted(
    [
        getattr(v, "__name__", k)
        for k, v in list(globals().items())  # export
        if (
            (
                callable(v)
                and getattr(v, "__module__", "")
                == __name__  # callables from this module
                or k.isupper()
            )
            and not str(getattr(v, "__name__", k)).startswith("__")  # or CONSTANTS
        )
    ]
)  # neither marked internal
