import json
from typing import Dict, NewType, List

from ontobio.model.association import GoAssociation, gp_type_label_to_curie


class Entity(dict):

    def __init__(self, d):
        super(Entity, self).__init__(d)

    def __hash__(self):
        d = json.dumps(self, sort_keys=True)
        return hash(d)


def convert_association(association):
    """
    'id' is already `join`ed in both the Association and the Entity,
    so we don't have to worry about what that looks like. We assume
    it's correct.
    """

    if isinstance(association, GoAssociation):
        # print(json.dumps(association, indent=4))
        gpi_obj = {
            'id': str(association.subject.id),
            'label': association.subject.label,  # db_object_symbol,
            'full_name': association.subject.fullname,  # db_object_name,
            'synonyms': association.subject.synonyms,
            'type': [gp_type_label_to_curie(association.subject.type[0])], #db_object_type,
            'parents': "",  # GAF does not have this field, but it's optional in GPI
            'xrefs': "",  # GAF does not have this field, but it's optional in GPI
            'taxon': {
                'id': str(association.subject.taxon)
            }
        }
        return Entity(gpi_obj)

    return None


class GafGpiBridge(object):

    def __init__(self):
        self.cache = []

    def entities(self):
        return list(self.cache)



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
