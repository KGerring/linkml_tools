from ontobio.rdfgen import relations
from ontobio.model import association
from ontobio.rdfgen.relations import lookup_label


def test_lookup_label():
    label = 'directly negatively regulates'
    expected_url = 'http://purl.obolibrary.org/obo/RO_0002630'
    expected_curie = 'RO:0002630'
    # Call the function and check the return value
    result = lookup_label(label)
    curie = str(relations.obo_uri_to_curie(result))
    assert curie == expected_curie, f"Expected {expected_curie}, but got {curie}"
    assert result == expected_url, f"Expected {expected_url}, but got {result}"


def test_relations_curie_expand():
    uri = relations.curie_to_obo_uri(association.Curie.from_str("GO:1234567"))
    assert uri == "http://purl.obolibrary.org/obo/GO_1234567"


def test_relations_curie_contract():
    curie = relations.obo_uri_to_curie("http://purl.obolibrary.org/obo/GO_1234567")
    assert curie == association.Curie(namespace="GO", identity="1234567")


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


