from prefixcommons import curie_util
from prefixcommons.curie_util import contract_uri, expand_uri, get_prefixes
from ontobio.vocabulary.relations import OboRO, Evidence
from ontobio.vocabulary.upper import UpperLevel
from ontobio.ecomap import EcoMap
from ontobio.rdfgen import relations
from ontobio.model import association as association_model
from rdflib import Namespace
from rdflib import BNode
from rdflib import Literal
from rdflib import URIRef
from rdflib.namespace import RDF
from rdflib.namespace import RDFS
from rdflib.namespace import OWL
import rdflib
import logging
import uuid
import re
import json

ro = OboRO()
evt = Evidence()
upt = UpperLevel()

# Pull the go_context file from prefixcommons.
# NOTE: this is a temporary measure. We will build the go json ld context as part of the pipeline in future
# See https://github.com/geneontology/go-site/issues/617
prefix_context = {key: value for context in curie_util.default_curie_maps + [curie_util.read_biocontext("go_context")] for key, value in context.items()}

HAS_SUPPORTING_REFERENCE = URIRef(expand_uri(evt.has_supporting_reference, cmaps=[evt._prefixmap]))

ENABLED_BY = URIRef(expand_uri(ro.enabled_by))
ENABLES = URIRef(expand_uri(ro.enables))
INVOLVED_IN = URIRef(expand_uri(ro.involved_in))
PART_OF = URIRef(expand_uri(ro.part_of))
OCCURS_IN = URIRef(expand_uri(ro.occurs_in))
COLOCALIZES_WITH = URIRef(expand_uri(ro.colocalizes_with))
MOLECULAR_FUNCTION = URIRef(expand_uri(upt.molecular_function))

logger = logging.getLogger(__name__)


def genid(base=None):
    return URIRef(str(uuid.uuid4()), base=base)

class RdfWriter(object):
    """
    Abstract base class for all RdfWriters
    """
    pass


class TurtleRdfWriter(RdfWriter):
    """
    Default implementation of RdfWriter

    use rdflib to generate a turtle file
    """
    def __init__(self, label=None):
        self.base = genid(base="http://model.geneontology.org") + '/'
        self.graph = rdflib.Graph(identifier=self.base)
        self.graph.bind("owl", OWL)
        self.graph.bind("obo", "http://purl.obolibrary.org/obo/")

        self.graph.add((self.base, RDF.type, OWL.Ontology))
        if label != None:
            self.graph.add((self.base, RDFS.label, Literal(label)))

    def add(self, s, p, o):
        self.graph.add((s, p, o))

    def serialize(self, destination=None, format='ttl', **args):

        if destination != None:
            self.graph.serialize(destination, format, **args)
        else:
            return self.graph.serialize(destination, format, **args)


class RdfTransform(object):
    """
    base class for all RDF generators
    """

    def __init__(self, writer=None):
        if writer is None:
            writer = TurtleRdfWriter()

        self.writer = writer
        self.include_subject_info = False
        self.ecomap = EcoMap()
        self._emit_header_done = False
        self.uribase = writer.base
        self.ecomap.mappings()
        self.bad_chars_regex = re.compile("[^\.:_\-0-9a-zA-Z]")
        self.ro_lookup = dict(relations.label_relation_lookup())

    def blanknode(self):
        return BNode()

    def uri(self, id):
        # allow either atoms or objects
        if isinstance(id, dict):
            return self.uri(id['id'])
        # logger.info("Expand: {}".format(id))

        id = self.bad_chars_regex.sub("_", id)
        uri = curie_util.expand_uri(id, cmaps=[prefix_context])
        if uri != id:
            # If URI is different, then that means we found an curie expansion, and we should add the prefix
            prefix = id.split(":")[0]
            self.writer.graph.bind(prefix, prefix_context[prefix])

        return URIRef(uri)

    def lookup_relation(self, label):
        label = label.replace('_', ' ')

        # Return the cached label -> URI or None
        if label in self.ro_lookup:
            return self.uri(self.ro_lookup[label])
        else:
            return None

    def emit(self, s, p, o):
        logger.debug("TRIPLE: {} {} {}".format(s,p,o))
        self.writer.add(s,p,o)
        return (s,p,o)

    def emit_type(self, s, t):
        return self.emit(s, RDF.type, t)

    def emit_label(self, s, o):
        return self.emit(s, RDFS.label, Literal(o))

    def emit_not(self, s, t):
        bn = self.blanknode()
        self.emit_type(bn, OWL.Class)
        self.emit(bn, OWL.complementOf, URIRef(expand_uri(t)))
        return self.emit_type(s, bn)

    def eco_class(self, code, coderef=None):
        eco_cls_id = self.ecomap.coderef_to_ecoclass(code, coderef)
        logger.debug(self.ecomap._mappings)
        logger.debug('ECO: {},{}->{}'.format(code, coderef, eco_cls_id))
        return self.uri(eco_cls_id)

    def translate_evidence(self, association, stmt):
        """

        ``
        _:1 a Axiom
            owl:annotatedSource s
            owl:annotatedProperty p
            owl:annotatedTarget o
            evidence [ a ECO ; ...]
        ``

        """
        ev = association['evidence']
        ev_id = None
        if 'id' in ev:
            ev_id = self.uri(ev['id'])
        else:
            ev_id = genid(base=self.writer.base + '/')

        stmt_id = self.blanknode() ## OWL reification: must be blank
        (s,p,o) = stmt
        self.emit_type(stmt_id, OWL.Axiom)

        self.emit(stmt_id, OWL.annotatedSource, s)
        self.emit(stmt_id, OWL.annotatedProperty, p)
        self.emit(stmt_id, OWL.annotatedTarget, o)

        self.emit(stmt_id, self.uri(evt.axiom_has_evidence), ev_id)

        ev_cls = self.eco_class(self.uri(ev['type']))
        self.emit_type(ev_id, OWL.NamedIndividual)
        self.emit_type(ev_id, ev_cls)
        if 'with_support_from' in ev:
            for w in ev['with_support_from']:
                self.emit(ev_id, self.uri(evt.evidence_with_support_from), self.uri(w))
        for ref in ev['has_supporting_reference']:
            o = self.uri(ref)
            if ref == expand_uri(ref):
                o = Literal(ref)
            self.emit(ev_id, HAS_SUPPORTING_REFERENCE, o)
        if 'with_support_from' in ev:
            for ref in ev['with_support_from']:
                self.emit(ev_id, self.uri(evt.evidence_with_support_from), self.uri(ref))


class CamRdfTransform(RdfTransform):
    """
    Granular instance-based representation (GO-CAM)

    Perform gappy translation from simple assocs model to GOCAM

    See https://github.com/geneontology/minerva/blob/master/specs/owl-model.md
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bad_properties_found = set()

    def emit_header(self):
        if self._emit_header_done:
            return
        self._emit_header_done = True
        self.emit_type(ENABLED_BY, OWL.ObjectProperty)
        self.emit_type(PART_OF, OWL.ObjectProperty)
        self.emit_type(OCCURS_IN, OWL.ObjectProperty)

    def translate(self, association: association_model.GoAssociation):

        # See https://github.com/biolink/ontobio/pull/136
        # if the association has an annotation extension, and this
        # is a union, then we treat each element in the union
        # as a distinct assertion/annotation, where each assertion
        # has its own conjunction of relational expressions

        if isinstance(association, dict) and "header" in association:
            return
            
        association = association.to_hash_assoc() # type: Dict

        object_extensions = association.get('object_extensions', {})

        conjunctive_sets = []  # Will be a list of lists, e.g. [[rel1(GO:1), rel2(GO:2)], [rel1(GO:3)]]
        for cj in object_extensions.get("union_of", []):
            conjunctive_sets.append(cj['intersection_of'])
        if not conjunctive_sets:
            conjunctive_sets.append([])  # A dummy list val to trigger one go through the loop

        for conjunctive_set in conjunctive_sets:
            # and_xps = ix.get'intersection_of']
            # self.translate(association, and_xps)

            sub = association['subject']
            obj = association['object']
            rel = association['relation']
            sub_uri = self.uri(sub)
            obj_uri = self.uri(obj)

            # E.g. instance of gene product class
            enabler_id = genid(base=self.writer.base)
            self.emit_type(enabler_id, sub_uri)
            self.emit_type(enabler_id, OWL.NamedIndividual)

            # subject GP class label and taxon restriction
            self.emit_label(sub_uri, sub["label"])
            if "taxon" in sub:
                restriction = rdflib.BNode()
                self.emit_type(restriction, OWL.Restriction)
                self.emit(restriction, OWL.onProperty, self.uri(ro.in_taxon))
                self.emit(restriction, OWL.someValuesFrom, self.uri(sub["taxon"]["id"]))
                self.emit(sub_uri, RDFS.subClassOf, restriction)

            # E.g. instance of GO class
            tgt_id = genid(base=self.writer.base)
            self.emit_type(tgt_id, obj_uri)
            self.emit_type(tgt_id, OWL.NamedIndividual)

            aspect = association['aspect']
            aspect_triple = None

            # todo: use relation
            if aspect == 'F':
                aspect_triple = self.emit(tgt_id, ENABLED_BY, enabler_id)
            elif aspect == 'P':
                mf_id = genid(base=self.writer.base)
                self.emit_type(mf_id, MOLECULAR_FUNCTION)
                aspect_triple = self.emit(mf_id, ENABLED_BY, enabler_id)
                aspect_triple = self.emit(mf_id, PART_OF, tgt_id)
            elif aspect == 'C':
                mf_id = genid(base=self.writer.base)
                self.emit_type(mf_id, MOLECULAR_FUNCTION)
                aspect_triple = self.emit(mf_id, ENABLED_BY, enabler_id)
                aspect_triple = self.emit(mf_id, OCCURS_IN, tgt_id)
            else:
                # Skip this association if the aspect makes no sense.
                logger.warning("Aspect field is not F, P, or C, so this association is skipped.")
                return

            if self.include_subject_info:
                pass
                # TODO

            if association['object_extensions'] != {}:
                pass
            if conjunctive_set != []:
                for ext in conjunctive_set:
                    filler_inst = genid(base=self.writer.base)
                    self.emit_type(filler_inst, self.uri(ext['filler']))
                    p = self.lookup_relation(ext['property'])
                    if p is None:
                        if ext["property"] not in self.bad_properties_found:
                            self.bad_properties_found.add(ext["property"])
                            logger.warning("No such property {}".format(ext))
                    else:
                        self.emit(tgt_id, p, filler_inst)
            self.translate_evidence(association, aspect_triple)

    def provenance(self):
        self.writer.graph.bind("metago", "http://model.geneontology.org/")
        self.writer.graph.add((self.writer.base, URIRef("http://model.geneontology.org/graphType"), URIRef("http://model.geneontology.org/gafCam")))

class SimpleAssocRdfTransform(RdfTransform):
    """
    Follows simple OBAN-style model

    See: https://github.com/EBISPOT/OBAN

    See also: https://github.com/monarch-initiative/dipper/
    """

    def emit_header(self):
        if self._emit_header_done:
            return
        self._emit_header_done = True

    def translate(self, association: association_model.GoAssociation):
        association = association.to_hash_assoc()

        sub = association['subject']
        obj = association['subject']
        rel = association['relation']['id']
        sub_uri = self.uri(sub)
        obj_uri = self.uri(obj)

        rel_url = None
        rel_uri = None
        if rel == 'part_of':
            rel_uri = PART_OF
        elif rel == 'enables':
            rel_uri = ENABLES
        elif rel == 'involved_in':
            rel_uri = INVOLVED_IN
        elif rel == 'colocalizes_with':
            rel_uri = COLOCALIZES_WITH
        else:
            logger.error("Unknown: {}".format(rel))

        # TODO: extensions
        stmt = self.emit(sub_uri,rel_uri,obj_uri)

        # optionally include info about subject (e.g. gene)
        if self.include_subject_info:
            self.emit_label(sub_uri, sub)
            if 'taxon' in sub:
                taxon = sub['taxon']
                self.emit(sub_uri, ro.in_taxon, self.uri(taxon))
            # TODO syns etc

        self.translate_evidence(association, stmt)



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
