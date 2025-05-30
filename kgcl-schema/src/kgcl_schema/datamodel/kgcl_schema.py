# Auto generated from kgcl_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-09-14T16:13:52
# Schema: kgcl-schema
#
# id: https://w3id.org/hrshdhgd/kgcl-schema
# description: A linkml based schema for Knowledge Graph Change Language (KGCL). A data model for describing
#              change operations at a high level on an ontology or ontology-like artefact, such as a Knowledge
#              Graph.
# license: MIT

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BASICS = CurieNamespace('basics', 'https://w3id.org/kgcl_schema/basics/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
KGCL_SCHEMA = CurieNamespace('kgcl_schema', 'https://w3id.org/kgcl-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OIO = CurieNamespace('oio', 'http://www.geneontology.org/formats/oboInOwl#')
OM = CurieNamespace('om', 'http://w3id.org/kgcl_schema/om/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XML = CurieNamespace('xml', 'http://example.org/UNKNOWN/xml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = KGCL_SCHEMA


# Types
class ChangeClassType(Uriorcurie):
    """ CURIE for a class within this datamodel. E.g. kgcl:NodeObsoletion """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "change class type"
    type_model_uri = KGCL_SCHEMA.ChangeClassType


class LanguageTag(str):
    type_class_uri = XML.lang
    type_class_curie = "xml:lang"
    type_name = "language tag"
    type_model_uri = KGCL_SCHEMA.LanguageTag


# Class references
class ChangeId(extended_str):
    pass


class SimpleChangeId(ChangeId):
    pass


class ComplexChangeId(ChangeId):
    pass


class MultiNodeObsoletionId(ComplexChangeId):
    pass


class TransactionId(ChangeId):
    pass


class EdgeChangeId(SimpleChangeId):
    pass


class EdgeCreationId(EdgeChangeId):
    pass


class PlaceUnderId(EdgeCreationId):
    pass


class EdgeDeletionId(EdgeChangeId):
    pass


class RemoveUnderId(EdgeDeletionId):
    pass


class EdgeObsoletionId(EdgeChangeId):
    pass


class EdgeRewiringId(EdgeChangeId):
    pass


class MappingCreationId(EdgeCreationId):
    pass


class NodeMoveId(EdgeChangeId):
    pass


class NodeDeepeningId(NodeMoveId):
    pass


class NodeShallowingId(NodeMoveId):
    pass


class PredicateChangeId(EdgeChangeId):
    pass


class EdgeLogicalInterpretationChangeId(EdgeChangeId):
    pass


class LogicalAxiomChangeId(SimpleChangeId):
    pass


class NodeChangeId(SimpleChangeId):
    pass


class NodeRenameId(NodeChangeId):
    pass


class SetLanguageForNameId(NodeChangeId):
    pass


class NodeAnnotationChangeId(NodeChangeId):
    pass


class NodeAnnotationReplacementId(NodeAnnotationChangeId):
    pass


class NodeSynonymChangeId(NodeChangeId):
    pass


class NewSynonymId(NodeSynonymChangeId):
    pass


class NameBecomesSynonymId(NodeSynonymChangeId):
    pass


class RemoveSynonymId(NodeSynonymChangeId):
    pass


class SynonymReplacementId(NodeSynonymChangeId):
    pass


class SynonymPredicateChangeId(NodeSynonymChangeId):
    pass


class NodeTextDefinitionChangeId(NodeChangeId):
    pass


class NewTextDefinitionId(NodeTextDefinitionChangeId):
    pass


class RemoveTextDefinitionId(NodeTextDefinitionChangeId):
    pass


class TextDefinitionReplacementId(NodeTextDefinitionChangeId):
    pass


class AddNodeToSubsetId(NodeChangeId):
    pass


class RemovedNodeFromSubsetId(NodeChangeId):
    pass


class NodeObsoletionId(NodeChangeId):
    pass


class NodeUnobsoletionId(NodeChangeId):
    pass


class NodeCreationId(NodeChangeId):
    pass


class ClassCreationId(NodeCreationId):
    pass


class NodeDeletionId(NodeChangeId):
    pass


class NodeDirectMergeId(NodeObsoletionId):
    pass


class NodeObsoletionWithDirectReplacementId(NodeObsoletionId):
    pass


class NodeObsoletionWithNoDirectReplacementId(NodeObsoletionId):
    pass


class NodeId(extended_str):
    pass


class ClassNodeId(NodeId):
    pass


class InstanceNodeId(NodeId):
    pass


class ActivityId(extended_str):
    pass


class AgentId(extended_str):
    pass


@dataclass
class Change(YAMLRoot):
    """
    Any change perform on an ontology or knowledge graph
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.Change
    class_class_curie: ClassVar[str] = "kgcl_schema:Change"
    class_name: ClassVar[str] = "change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Change

    id: Union[str, ChangeId] = None
    type: Optional[str] = None
    was_generated_by: Optional[Union[str, ActivityId]] = None
    see_also: Optional[str] = None
    pull_request: Optional[str] = None
    creator: Optional[str] = None
    change_date: Optional[str] = None
    contributor: Optional[str] = None
    has_undo: Optional[Union[str, ChangeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChangeId):
            self.id = ChangeId(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.was_generated_by is not None and not isinstance(self.was_generated_by, ActivityId):
            self.was_generated_by = ActivityId(self.was_generated_by)

        if self.see_also is not None and not isinstance(self.see_also, str):
            self.see_also = str(self.see_also)

        if self.pull_request is not None and not isinstance(self.pull_request, str):
            self.pull_request = str(self.pull_request)

        if self.creator is not None and not isinstance(self.creator, str):
            self.creator = str(self.creator)

        if self.change_date is not None and not isinstance(self.change_date, str):
            self.change_date = str(self.change_date)

        if self.contributor is not None and not isinstance(self.contributor, str):
            self.contributor = str(self.contributor)

        if self.has_undo is not None and not isinstance(self.has_undo, ChangeId):
            self.has_undo = ChangeId(self.has_undo)

        super().__post_init__(**kwargs)


@dataclass
class SimpleChange(Change):
    """
    A change that is about a single ontology element
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.SimpleChange
    class_class_curie: ClassVar[str] = "kgcl_schema:SimpleChange"
    class_name: ClassVar[str] = "simple change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.SimpleChange

    id: Union[str, SimpleChangeId] = None
    old_value: Optional[str] = None
    new_value: Optional[str] = None
    old_value_type: Optional[str] = None
    new_value_type: Optional[str] = None
    new_language: Optional[str] = None
    old_language: Optional[str] = None
    new_datatype: Optional[str] = None
    old_datatype: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.old_value is not None and not isinstance(self.old_value, str):
            self.old_value = str(self.old_value)

        if self.new_value is not None and not isinstance(self.new_value, str):
            self.new_value = str(self.new_value)

        if self.old_value_type is not None and not isinstance(self.old_value_type, str):
            self.old_value_type = str(self.old_value_type)

        if self.new_value_type is not None and not isinstance(self.new_value_type, str):
            self.new_value_type = str(self.new_value_type)

        if self.new_language is not None and not isinstance(self.new_language, str):
            self.new_language = str(self.new_language)

        if self.old_language is not None and not isinstance(self.old_language, str):
            self.old_language = str(self.old_language)

        if self.new_datatype is not None and not isinstance(self.new_datatype, str):
            self.new_datatype = str(self.new_datatype)

        if self.old_datatype is not None and not isinstance(self.old_datatype, str):
            self.old_datatype = str(self.old_datatype)

        super().__post_init__(**kwargs)


@dataclass
class ComplexChange(Change):
    """
    A change that is is a composition of other changes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.ComplexChange
    class_class_curie: ClassVar[str] = "kgcl_schema:ComplexChange"
    class_name: ClassVar[str] = "complex change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.ComplexChange

    id: Union[str, ComplexChangeId] = None
    change_set: Optional[Union[Dict[Union[str, ChangeId], Union[dict, Change]], List[Union[dict, Change]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="change_set", slot_type=Change, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class MultiNodeObsoletion(ComplexChange):
    """
    A complex change consisting of multiple obsoletions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.MultiNodeObsoletion
    class_class_curie: ClassVar[str] = "kgcl_schema:MultiNodeObsoletion"
    class_name: ClassVar[str] = "multi node obsoletion"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.MultiNodeObsoletion

    id: Union[str, MultiNodeObsoletionId] = None
    change_set: Optional[Union[Dict[Union[str, NodeObsoletionId], Union[dict, "NodeObsoletion"]], List[Union[dict, "NodeObsoletion"]]]] = empty_dict()
    change_description: Optional[str] = None
    associated_change_set: Optional[Union[Dict[Union[str, ChangeId], Union[dict, Change]], List[Union[dict, Change]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MultiNodeObsoletionId):
            self.id = MultiNodeObsoletionId(self.id)

        self._normalize_inlined_as_list(slot_name="change_set", slot_type=NodeObsoletion, key_name="id", keyed=True)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        self._normalize_inlined_as_list(slot_name="associated_change_set", slot_type=Change, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Transaction(Change):
    """
    A change that is a composition of a set of changes, where those changes are treated as a single unit. Could be a
    single change, or the results of an ontology diff
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.Transaction
    class_class_curie: ClassVar[str] = "kgcl_schema:Transaction"
    class_name: ClassVar[str] = "transaction"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Transaction

    id: Union[str, TransactionId] = None
    change_set: Optional[Union[Dict[Union[str, ChangeId], Union[dict, Change]], List[Union[dict, Change]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TransactionId):
            self.id = TransactionId(self.id)

        self._normalize_inlined_as_list(slot_name="change_set", slot_type=Change, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class ChangeSetSummaryStatistic(YAMLRoot):
    """
    A summary statistic for a set of changes of the same type, grouped by zero or more node properties
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.ChangeSetSummaryStatistic
    class_class_curie: ClassVar[str] = "kgcl_schema:ChangeSetSummaryStatistic"
    class_name: ClassVar[str] = "change set summary statistic"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.ChangeSetSummaryStatistic

    change_type: Optional[Union[str, ChangeClassType]] = None
    count: Optional[int] = None
    property_value_set: Optional[Union[Union[dict, "PropertyValue"], List[Union[dict, "PropertyValue"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.change_type is not None and not isinstance(self.change_type, ChangeClassType):
            self.change_type = ChangeClassType(self.change_type)

        if self.count is not None and not isinstance(self.count, int):
            self.count = int(self.count)

        if not isinstance(self.property_value_set, list):
            self.property_value_set = [self.property_value_set] if self.property_value_set is not None else []
        self.property_value_set = [v if isinstance(v, PropertyValue) else PropertyValue(**as_dict(v)) for v in self.property_value_set]

        super().__post_init__(**kwargs)


class ChangeMixin(YAMLRoot):
    """
    root class for all change mixins
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.ChangeMixin
    class_class_curie: ClassVar[str] = "kgcl_schema:ChangeMixin"
    class_name: ClassVar[str] = "change mixin"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.ChangeMixin


@dataclass
class Obsoletion(ChangeMixin):
    """
    Obsoletion of an element deprecates usage of that element, but does not delete that element.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.Obsoletion
    class_class_curie: ClassVar[str] = "kgcl_schema:Obsoletion"
    class_name: ClassVar[str] = "obsoletion"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Obsoletion

    about: Optional[Union[dict, "OntologyElement"]] = None
    has_undo: Optional[Union[dict, "Obsoletion"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.about is not None and not isinstance(self.about, OntologyElement):
            self.about = OntologyElement()

        if self.has_undo is not None and not isinstance(self.has_undo, Obsoletion):
            self.has_undo = Obsoletion(**as_dict(self.has_undo))

        super().__post_init__(**kwargs)


class DatatypeOrLanguageTagChange(ChangeMixin):
    """
    A change in a value assertion where the value remain unchanged but either the datatype or language changes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.DatatypeOrLanguageTagChange
    class_class_curie: ClassVar[str] = "kgcl_schema:DatatypeOrLanguageTagChange"
    class_name: ClassVar[str] = "datatype or language tag change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.DatatypeOrLanguageTagChange


@dataclass
class LanguageTagChange(DatatypeOrLanguageTagChange):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.LanguageTagChange
    class_class_curie: ClassVar[str] = "kgcl_schema:LanguageTagChange"
    class_name: ClassVar[str] = "language tag change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.LanguageTagChange

    old_value: Optional[str] = None
    new_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.old_value is not None and not isinstance(self.old_value, str):
            self.old_value = str(self.old_value)

        if self.new_value is not None and not isinstance(self.new_value, str):
            self.new_value = str(self.new_value)

        super().__post_init__(**kwargs)


class DatatypeChange(DatatypeOrLanguageTagChange):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.DatatypeChange
    class_class_curie: ClassVar[str] = "kgcl_schema:DatatypeChange"
    class_name: ClassVar[str] = "datatype change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.DatatypeChange


class AllowsAutomaticReplacementOfEdges(Obsoletion):
    """
    Applies to an obsoletion in which annotations or edges pointing at the obsoleted node can be automatically rewired
    to point to a target
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.AllowsAutomaticReplacementOfEdges
    class_class_curie: ClassVar[str] = "kgcl_schema:AllowsAutomaticReplacementOfEdges"
    class_name: ClassVar[str] = "allows automatic replacement of edges"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.AllowsAutomaticReplacementOfEdges


@dataclass
class Unobsoletion(ChangeMixin):
    """
    Opposite operation of obsoletion. Rarely performed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.Unobsoletion
    class_class_curie: ClassVar[str] = "kgcl_schema:Unobsoletion"
    class_name: ClassVar[str] = "unobsoletion"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Unobsoletion

    has_undo: Optional[Union[dict, Obsoletion]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_undo is not None and not isinstance(self.has_undo, Obsoletion):
            self.has_undo = Obsoletion(**as_dict(self.has_undo))

        super().__post_init__(**kwargs)


class Deletion(ChangeMixin):
    """
    Removal of an element.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.Deletion
    class_class_curie: ClassVar[str] = "kgcl_schema:Deletion"
    class_name: ClassVar[str] = "deletion"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Deletion


@dataclass
class Creation(ChangeMixin):
    """
    Creation of an element.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.Creation
    class_class_curie: ClassVar[str] = "kgcl_schema:Creation"
    class_name: ClassVar[str] = "creation"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Creation

    has_undo: Optional[Union[dict, Deletion]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_undo is not None and not isinstance(self.has_undo, Deletion):
            self.has_undo = Deletion()

        super().__post_init__(**kwargs)


@dataclass
class SubsetMembershipChange(ChangeMixin):
    """
    A change in the membership status of a node with respect to a subset (view)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.SubsetMembershipChange
    class_class_curie: ClassVar[str] = "kgcl_schema:SubsetMembershipChange"
    class_name: ClassVar[str] = "subset membership change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.SubsetMembershipChange

    in_subset: Optional[Union[dict, "OntologySubset"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.in_subset is not None and not isinstance(self.in_subset, OntologySubset):
            self.in_subset = OntologySubset()

        super().__post_init__(**kwargs)


@dataclass
class AddToSubset(SubsetMembershipChange):
    """
    placing an element inside a subset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.AddToSubset
    class_class_curie: ClassVar[str] = "kgcl_schema:AddToSubset"
    class_name: ClassVar[str] = "add to subset"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.AddToSubset

    in_subset: Optional[Union[dict, "OntologySubset"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.in_subset is not None and not isinstance(self.in_subset, OntologySubset):
            self.in_subset = OntologySubset()

        super().__post_init__(**kwargs)


@dataclass
class RemoveFromSubset(SubsetMembershipChange):
    """
    removing an element from a subset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.RemoveFromSubset
    class_class_curie: ClassVar[str] = "kgcl_schema:RemoveFromSubset"
    class_name: ClassVar[str] = "remove from subset"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.RemoveFromSubset

    in_subset: Optional[Union[dict, "OntologySubset"]] = None
    has_undo: Optional[Union[dict, AddToSubset]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.in_subset is not None and not isinstance(self.in_subset, OntologySubset):
            self.in_subset = OntologySubset()

        if self.has_undo is not None and not isinstance(self.has_undo, AddToSubset):
            self.has_undo = AddToSubset(**as_dict(self.has_undo))

        super().__post_init__(**kwargs)


@dataclass
class EdgeChange(SimpleChange):
    """
    A change in which the element that is the focus of the change is an edge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.EdgeChange
    class_class_curie: ClassVar[str] = "kgcl_schema:EdgeChange"
    class_name: ClassVar[str] = "edge change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.EdgeChange

    id: Union[str, EdgeChangeId] = None
    about_edge: Optional[Union[dict, "Edge"]] = None
    object_type: Optional[str] = None
    language: Optional[str] = None
    datatype: Optional[str] = None
    subject: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.about_edge is not None and not isinstance(self.about_edge, Edge):
            self.about_edge = Edge(**as_dict(self.about_edge))

        if self.object_type is not None and not isinstance(self.object_type, str):
            self.object_type = str(self.object_type)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.datatype is not None and not isinstance(self.datatype, str):
            self.datatype = str(self.datatype)

        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class EdgeCreation(EdgeChange):
    """
    An edge change in which a de-novo edge is created. The edge is potentially annotated in the same action.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.EdgeCreation
    class_class_curie: ClassVar[str] = "kgcl_schema:EdgeCreation"
    class_name: ClassVar[str] = "edge creation"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.EdgeCreation

    id: Union[str, EdgeCreationId] = None
    subject: Optional[Union[str, NodeId]] = None
    predicate: Optional[Union[str, NodeId]] = None
    object: Optional[Union[str, NodeId]] = None
    subject_type: Optional[str] = None
    predicate_type: Optional[str] = None
    object_type: Optional[str] = None
    annotation_set: Optional[Union[dict, "Annotation"]] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EdgeCreationId):
            self.id = EdgeCreationId(self.id)

        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, NodeId):
            self.predicate = NodeId(self.predicate)

        if self.object is not None and not isinstance(self.object, NodeId):
            self.object = NodeId(self.object)

        if self.subject_type is not None and not isinstance(self.subject_type, str):
            self.subject_type = str(self.subject_type)

        if self.predicate_type is not None and not isinstance(self.predicate_type, str):
            self.predicate_type = str(self.predicate_type)

        if self.object_type is not None and not isinstance(self.object_type, str):
            self.object_type = str(self.object_type)

        if self.annotation_set is not None and not isinstance(self.annotation_set, Annotation):
            self.annotation_set = Annotation(**as_dict(self.annotation_set))

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class PlaceUnder(EdgeCreation):
    """
    An edge creation where the predicate is owl:subClassOf
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.PlaceUnder
    class_class_curie: ClassVar[str] = "kgcl_schema:PlaceUnder"
    class_name: ClassVar[str] = "place under"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.PlaceUnder

    id: Union[str, PlaceUnderId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlaceUnderId):
            self.id = PlaceUnderId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EdgeDeletion(EdgeChange):
    """
    An edge change in which an edge is removed. All edge annotations/properies are removed in the same action.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.EdgeDeletion
    class_class_curie: ClassVar[str] = "kgcl_schema:EdgeDeletion"
    class_name: ClassVar[str] = "edge deletion"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.EdgeDeletion

    id: Union[str, EdgeDeletionId] = None
    subject: Optional[Union[str, NodeId]] = None
    predicate: Optional[Union[str, NodeId]] = None
    object: Optional[Union[str, NodeId]] = None
    subject_type: Optional[str] = None
    predicate_type: Optional[str] = None
    object_type: Optional[str] = None
    annotation_set: Optional[Union[dict, "Annotation"]] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EdgeDeletionId):
            self.id = EdgeDeletionId(self.id)

        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, NodeId):
            self.predicate = NodeId(self.predicate)

        if self.object is not None and not isinstance(self.object, NodeId):
            self.object = NodeId(self.object)

        if self.subject_type is not None and not isinstance(self.subject_type, str):
            self.subject_type = str(self.subject_type)

        if self.predicate_type is not None and not isinstance(self.predicate_type, str):
            self.predicate_type = str(self.predicate_type)

        if self.object_type is not None and not isinstance(self.object_type, str):
            self.object_type = str(self.object_type)

        if self.annotation_set is not None and not isinstance(self.annotation_set, Annotation):
            self.annotation_set = Annotation(**as_dict(self.annotation_set))

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class RemoveUnder(EdgeDeletion):
    """
    An edge deletion where the predicate is owl:subClassOf
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.RemoveUnder
    class_class_curie: ClassVar[str] = "kgcl_schema:RemoveUnder"
    class_name: ClassVar[str] = "remove under"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.RemoveUnder

    id: Union[str, RemoveUnderId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RemoveUnderId):
            self.id = RemoveUnderId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EdgeObsoletion(EdgeChange):
    """
    An edge change in which an edge is obsoleted.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.EdgeObsoletion
    class_class_curie: ClassVar[str] = "kgcl_schema:EdgeObsoletion"
    class_name: ClassVar[str] = "edge obsoletion"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.EdgeObsoletion

    id: Union[str, EdgeObsoletionId] = None
    subject: Optional[Union[str, NodeId]] = None
    predicate: Optional[Union[str, NodeId]] = None
    object: Optional[Union[str, NodeId]] = None
    annotation_set: Optional[Union[dict, "Annotation"]] = None
    change_description: Optional[str] = None
    about: Optional[Union[dict, "OntologyElement"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EdgeObsoletionId):
            self.id = EdgeObsoletionId(self.id)

        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, NodeId):
            self.predicate = NodeId(self.predicate)

        if self.object is not None and not isinstance(self.object, NodeId):
            self.object = NodeId(self.object)

        if self.annotation_set is not None and not isinstance(self.annotation_set, Annotation):
            self.annotation_set = Annotation(**as_dict(self.annotation_set))

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        if self.about is not None and not isinstance(self.about, OntologyElement):
            self.about = OntologyElement()

        super().__post_init__(**kwargs)


@dataclass
class EdgeRewiring(EdgeChange):
    """
    An edge change where one node is replaced with another, as in the case of obsoletion with replacement
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.EdgeRewiring
    class_class_curie: ClassVar[str] = "kgcl_schema:EdgeRewiring"
    class_name: ClassVar[str] = "edge rewiring"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.EdgeRewiring

    id: Union[str, EdgeRewiringId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EdgeRewiringId):
            self.id = EdgeRewiringId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MappingCreation(EdgeCreation):
    """
    A specific kind of edge creation in which the created edge is a mapping.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.MappingCreation
    class_class_curie: ClassVar[str] = "kgcl_schema:MappingCreation"
    class_name: ClassVar[str] = "mapping creation"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.MappingCreation

    id: Union[str, MappingCreationId] = None
    subject: Optional[Union[str, NodeId]] = None
    predicate: Optional[Union[str, NodeId]] = None
    object: Optional[Union[str, NodeId]] = None
    annotation_set: Optional[Union[dict, "Annotation"]] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MappingCreationId):
            self.id = MappingCreationId(self.id)

        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, NodeId):
            self.predicate = NodeId(self.predicate)

        if self.object is not None and not isinstance(self.object, NodeId):
            self.object = NodeId(self.object)

        if self.annotation_set is not None and not isinstance(self.annotation_set, Annotation):
            self.annotation_set = Annotation(**as_dict(self.annotation_set))

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class NodeMove(EdgeChange):
    """
    A node move is a combination of deleting a parent edge and adding a parent edge, where the predicate is preserved
    and the object/parent node changes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeMove
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeMove"
    class_name: ClassVar[str] = "node move"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeMove

    id: Union[str, NodeMoveId] = None
    old_object_type: Optional[str] = None
    new_object_type: Optional[str] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeMoveId):
            self.id = NodeMoveId(self.id)

        if self.old_object_type is not None and not isinstance(self.old_object_type, str):
            self.old_object_type = str(self.old_object_type)

        if self.new_object_type is not None and not isinstance(self.new_object_type, str):
            self.new_object_type = str(self.new_object_type)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class NodeDeepening(NodeMove):
    """
    A node move in which a node where the destination is a proper descendant of the original location. Note that here
    descendant applied not just to subclass, but edges of any predicate in the relational graph
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeDeepening
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeDeepening"
    class_name: ClassVar[str] = "node deepening"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeDeepening

    id: Union[str, NodeDeepeningId] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeDeepeningId):
            self.id = NodeDeepeningId(self.id)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class NodeShallowing(NodeMove):
    """
    The opposite of node deepening
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeShallowing
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeShallowing"
    class_name: ClassVar[str] = "node shallowing"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeShallowing

    id: Union[str, NodeShallowingId] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeShallowingId):
            self.id = NodeShallowingId(self.id)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class PredicateChange(EdgeChange):
    """
    An edge change where the predicate (relationship type) is modified.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.PredicateChange
    class_class_curie: ClassVar[str] = "kgcl_schema:PredicateChange"
    class_name: ClassVar[str] = "predicate change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.PredicateChange

    id: Union[str, PredicateChangeId] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PredicateChangeId):
            self.id = PredicateChangeId(self.id)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class EdgeLogicalInterpretationChange(EdgeChange):
    """
    An edge change where the subjet, object, and predicate are unchanged, but the logical interpretation changes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.EdgeLogicalInterpretationChange
    class_class_curie: ClassVar[str] = "kgcl_schema:EdgeLogicalInterpretationChange"
    class_name: ClassVar[str] = "edge logical interpretation change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.EdgeLogicalInterpretationChange

    id: Union[str, EdgeLogicalInterpretationChangeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EdgeLogicalInterpretationChangeId):
            self.id = EdgeLogicalInterpretationChangeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class LogicalAxiomChange(SimpleChange):
    """
    A simple change where a logical axiom is changed, where the logical axiom cannot be represented as an edge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.LogicalAxiomChange
    class_class_curie: ClassVar[str] = "kgcl_schema:LogicalAxiomChange"
    class_name: ClassVar[str] = "logical axiom change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.LogicalAxiomChange

    id: Union[str, LogicalAxiomChangeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LogicalAxiomChangeId):
            self.id = LogicalAxiomChangeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class NodeChange(SimpleChange):
    """
    A simple change where the change is about a node
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeChange
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeChange"
    class_name: ClassVar[str] = "node change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeChange

    id: Union[str, NodeChangeId] = None
    about_node: Optional[Union[str, NodeId]] = None
    about_node_representation: Optional[str] = None
    language: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.about_node is not None and not isinstance(self.about_node, NodeId):
            self.about_node = NodeId(self.about_node)

        if self.about_node_representation is not None and not isinstance(self.about_node_representation, str):
            self.about_node_representation = str(self.about_node_representation)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        super().__post_init__(**kwargs)


@dataclass
class NodeRename(NodeChange):
    """
    A node change where the name (aka rdfs:label) of the node changes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeRename
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeRename"
    class_name: ClassVar[str] = "node rename"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeRename

    id: Union[str, NodeRenameId] = None
    old_value: Optional[str] = None
    new_value: Optional[str] = None
    has_textual_diff: Optional[Union[dict, "TextualDiff"]] = None
    new_language: Optional[str] = None
    old_language: Optional[str] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeRenameId):
            self.id = NodeRenameId(self.id)

        if self.old_value is not None and not isinstance(self.old_value, str):
            self.old_value = str(self.old_value)

        if self.new_value is not None and not isinstance(self.new_value, str):
            self.new_value = str(self.new_value)

        if self.has_textual_diff is not None and not isinstance(self.has_textual_diff, TextualDiff):
            self.has_textual_diff = TextualDiff()

        if self.new_language is not None and not isinstance(self.new_language, str):
            self.new_language = str(self.new_language)

        if self.old_language is not None and not isinstance(self.old_language, str):
            self.old_language = str(self.old_language)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class SetLanguageForName(NodeChange):
    """
    A node change where the string value for the name is unchanged but the language tag is set
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.SetLanguageForName
    class_class_curie: ClassVar[str] = "kgcl_schema:SetLanguageForName"
    class_name: ClassVar[str] = "set language for name"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.SetLanguageForName

    id: Union[str, SetLanguageForNameId] = None
    old_value: Optional[str] = None
    new_value: Optional[str] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SetLanguageForNameId):
            self.id = SetLanguageForNameId(self.id)

        if self.old_value is not None and not isinstance(self.old_value, str):
            self.old_value = str(self.old_value)

        if self.new_value is not None and not isinstance(self.new_value, str):
            self.new_value = str(self.new_value)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class NodeAnnotationChange(NodeChange):
    """
    A node change where the change alters node properties/annotations. TODO
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeAnnotationChange
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeAnnotationChange"
    class_name: ClassVar[str] = "node annotation change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeAnnotationChange

    id: Union[str, NodeAnnotationChangeId] = None
    annotation_property: Optional[str] = None
    annotation_property_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeAnnotationChangeId):
            self.id = NodeAnnotationChangeId(self.id)

        if self.annotation_property is not None and not isinstance(self.annotation_property, str):
            self.annotation_property = str(self.annotation_property)

        if self.annotation_property_type is not None and not isinstance(self.annotation_property_type, str):
            self.annotation_property_type = str(self.annotation_property_type)

        super().__post_init__(**kwargs)


@dataclass
class NodeAnnotationReplacement(NodeAnnotationChange):
    """
    A node annotation change where the change replaces a particular property value. TODO
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeAnnotationReplacement
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeAnnotationReplacement"
    class_name: ClassVar[str] = "node annotation replacement"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeAnnotationReplacement

    id: Union[str, NodeAnnotationReplacementId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeAnnotationReplacementId):
            self.id = NodeAnnotationReplacementId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class NodeSynonymChange(NodeChange):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeSynonymChange
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeSynonymChange"
    class_name: ClassVar[str] = "node synonym change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeSynonymChange

    id: Union[str, NodeSynonymChangeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeSynonymChangeId):
            self.id = NodeSynonymChangeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class NewSynonym(NodeSynonymChange):
    """
    A node synonym change where a de-novo synonym is created
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NewSynonym
    class_class_curie: ClassVar[str] = "kgcl_schema:NewSynonym"
    class_name: ClassVar[str] = "new synonym"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NewSynonym

    id: Union[str, NewSynonymId] = None
    new_value: Optional[str] = None
    language: Optional[str] = None
    qualifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NewSynonymId):
            self.id = NewSynonymId(self.id)

        if self.new_value is not None and not isinstance(self.new_value, str):
            self.new_value = str(self.new_value)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.qualifier is not None and not isinstance(self.qualifier, str):
            self.qualifier = str(self.qualifier)

        super().__post_init__(**kwargs)


@dataclass
class NameBecomesSynonym(NodeSynonymChange):
    """
    A node synonym where the name NAME of an node NODE moves to a synonym, and NODE receives a new name. This change
    consists of compose of (1) a node rename where NAME is replaced by a different name (2) a new synonym
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NameBecomesSynonym
    class_class_curie: ClassVar[str] = "kgcl_schema:NameBecomesSynonym"
    class_name: ClassVar[str] = "name becomes synonym"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NameBecomesSynonym

    id: Union[str, NameBecomesSynonymId] = None
    change_1: Optional[Union[str, NodeRenameId]] = None
    change_2: Optional[Union[str, NewSynonymId]] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NameBecomesSynonymId):
            self.id = NameBecomesSynonymId(self.id)

        if self.change_1 is not None and not isinstance(self.change_1, NodeRenameId):
            self.change_1 = NodeRenameId(self.change_1)

        if self.change_2 is not None and not isinstance(self.change_2, NewSynonymId):
            self.change_2 = NewSynonymId(self.change_2)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class RemoveSynonym(NodeSynonymChange):
    """
    A node synonym change where a synonym is deleted
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.RemoveSynonym
    class_class_curie: ClassVar[str] = "kgcl_schema:RemoveSynonym"
    class_name: ClassVar[str] = "remove synonym"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.RemoveSynonym

    id: Union[str, RemoveSynonymId] = None
    old_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RemoveSynonymId):
            self.id = RemoveSynonymId(self.id)

        if self.old_value is not None and not isinstance(self.old_value, str):
            self.old_value = str(self.old_value)

        super().__post_init__(**kwargs)


@dataclass
class SynonymReplacement(NodeSynonymChange):
    """
    A node synonym change where the text of a synonym is changed
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.SynonymReplacement
    class_class_curie: ClassVar[str] = "kgcl_schema:SynonymReplacement"
    class_name: ClassVar[str] = "synonym replacement"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.SynonymReplacement

    id: Union[str, SynonymReplacementId] = None
    old_value: Optional[str] = None
    new_value: Optional[str] = None
    has_textual_diff: Optional[Union[dict, "TextualDiff"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SynonymReplacementId):
            self.id = SynonymReplacementId(self.id)

        if self.old_value is not None and not isinstance(self.old_value, str):
            self.old_value = str(self.old_value)

        if self.new_value is not None and not isinstance(self.new_value, str):
            self.new_value = str(self.new_value)

        if self.has_textual_diff is not None and not isinstance(self.has_textual_diff, TextualDiff):
            self.has_textual_diff = TextualDiff()

        super().__post_init__(**kwargs)


@dataclass
class SynonymPredicateChange(NodeSynonymChange):
    """
    A node synonym change where the predicate of a synonym is changed. Background: synonyms can be represented by a
    variety of predicates. For example, many OBO ontologies make use of predicates such as oio:hasExactSynonym,
    oio:hasRelatedSynonym, etc
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.SynonymPredicateChange
    class_class_curie: ClassVar[str] = "kgcl_schema:SynonymPredicateChange"
    class_name: ClassVar[str] = "synonym predicate change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.SynonymPredicateChange

    id: Union[str, SynonymPredicateChangeId] = None
    old_value: Optional[str] = None
    new_value: Optional[str] = None
    has_textual_diff: Optional[Union[dict, "TextualDiff"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SynonymPredicateChangeId):
            self.id = SynonymPredicateChangeId(self.id)

        if self.old_value is not None and not isinstance(self.old_value, str):
            self.old_value = str(self.old_value)

        if self.new_value is not None and not isinstance(self.new_value, str):
            self.new_value = str(self.new_value)

        if self.has_textual_diff is not None and not isinstance(self.has_textual_diff, TextualDiff):
            self.has_textual_diff = TextualDiff()

        super().__post_init__(**kwargs)


@dataclass
class NodeTextDefinitionChange(NodeChange):
    """
    A node change where the text definition is changed
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeTextDefinitionChange
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeTextDefinitionChange"
    class_name: ClassVar[str] = "node text definition change"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeTextDefinitionChange

    id: Union[str, NodeTextDefinitionChangeId] = None

@dataclass
class NewTextDefinition(NodeTextDefinitionChange):
    """
    A node change where a de-novo text definition is created
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NewTextDefinition
    class_class_curie: ClassVar[str] = "kgcl_schema:NewTextDefinition"
    class_name: ClassVar[str] = "new text definition"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NewTextDefinition

    id: Union[str, NewTextDefinitionId] = None
    new_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NewTextDefinitionId):
            self.id = NewTextDefinitionId(self.id)

        if self.new_value is not None and not isinstance(self.new_value, str):
            self.new_value = str(self.new_value)

        super().__post_init__(**kwargs)


@dataclass
class RemoveTextDefinition(NodeTextDefinitionChange):
    """
    A node change where a text definition is deleted
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.RemoveTextDefinition
    class_class_curie: ClassVar[str] = "kgcl_schema:RemoveTextDefinition"
    class_name: ClassVar[str] = "remove text definition"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.RemoveTextDefinition

    id: Union[str, RemoveTextDefinitionId] = None
    old_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RemoveTextDefinitionId):
            self.id = RemoveTextDefinitionId(self.id)

        if self.old_value is not None and not isinstance(self.old_value, str):
            self.old_value = str(self.old_value)

        super().__post_init__(**kwargs)


@dataclass
class TextDefinitionReplacement(NodeTextDefinitionChange):
    """
    A node change where a text definition is modified
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.TextDefinitionReplacement
    class_class_curie: ClassVar[str] = "kgcl_schema:TextDefinitionReplacement"
    class_name: ClassVar[str] = "text definition replacement"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.TextDefinitionReplacement

    id: Union[str, TextDefinitionReplacementId] = None
    old_value: Optional[str] = None
    new_value: Optional[str] = None
    has_textual_diff: Optional[Union[dict, "TextualDiff"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TextDefinitionReplacementId):
            self.id = TextDefinitionReplacementId(self.id)

        if self.old_value is not None and not isinstance(self.old_value, str):
            self.old_value = str(self.old_value)

        if self.new_value is not None and not isinstance(self.new_value, str):
            self.new_value = str(self.new_value)

        if self.has_textual_diff is not None and not isinstance(self.has_textual_diff, TextualDiff):
            self.has_textual_diff = TextualDiff()

        super().__post_init__(**kwargs)


@dataclass
class AddNodeToSubset(NodeChange):
    """
    Places a node inside a subset, by annotating that node
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.AddNodeToSubset
    class_class_curie: ClassVar[str] = "kgcl_schema:AddNodeToSubset"
    class_name: ClassVar[str] = "add node to subset"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.AddNodeToSubset

    id: Union[str, AddNodeToSubsetId] = None
    in_subset: Optional[Union[dict, "OntologySubset"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AddNodeToSubsetId):
            self.id = AddNodeToSubsetId(self.id)

        if self.in_subset is not None and not isinstance(self.in_subset, OntologySubset):
            self.in_subset = OntologySubset()

        super().__post_init__(**kwargs)


@dataclass
class RemovedNodeFromSubset(NodeChange):
    """
    Removes a node from a subset, by removing an annotation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.RemovedNodeFromSubset
    class_class_curie: ClassVar[str] = "kgcl_schema:RemovedNodeFromSubset"
    class_name: ClassVar[str] = "removed node from subset"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.RemovedNodeFromSubset

    id: Union[str, RemovedNodeFromSubsetId] = None
    change_description: Optional[str] = None
    about_node: Optional[Union[str, NodeId]] = None
    subset: Optional[str] = None
    in_subset: Optional[Union[dict, "OntologySubset"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RemovedNodeFromSubsetId):
            self.id = RemovedNodeFromSubsetId(self.id)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        if self.about_node is not None and not isinstance(self.about_node, NodeId):
            self.about_node = NodeId(self.about_node)

        if self.subset is not None and not isinstance(self.subset, str):
            self.subset = str(self.subset)

        if self.in_subset is not None and not isinstance(self.in_subset, OntologySubset):
            self.in_subset = OntologySubset()

        super().__post_init__(**kwargs)


@dataclass
class NodeObsoletion(NodeChange):
    """
    Obsoletion of a node deprecates usage of that node, but does not delete it.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeObsoletion
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeObsoletion"
    class_name: ClassVar[str] = "node obsoletion"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeObsoletion

    id: Union[str, NodeObsoletionId] = None
    has_direct_replacement: Optional[Union[str, NodeId]] = None
    has_nondirect_replacement: Optional[Union[Union[str, NodeId], List[Union[str, NodeId]]]] = empty_list()
    change_description: Optional[str] = None
    associated_change_set: Optional[Union[Dict[Union[str, ChangeId], Union[dict, Change]], List[Union[dict, Change]]]] = empty_dict()
    about: Optional[Union[dict, "OntologyElement"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeObsoletionId):
            self.id = NodeObsoletionId(self.id)

        if self.has_direct_replacement is not None and not isinstance(self.has_direct_replacement, NodeId):
            self.has_direct_replacement = NodeId(self.has_direct_replacement)

        if not isinstance(self.has_nondirect_replacement, list):
            self.has_nondirect_replacement = [self.has_nondirect_replacement] if self.has_nondirect_replacement is not None else []
        self.has_nondirect_replacement = [v if isinstance(v, NodeId) else NodeId(v) for v in self.has_nondirect_replacement]

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        self._normalize_inlined_as_list(slot_name="associated_change_set", slot_type=Change, key_name="id", keyed=True)

        if self.about is not None and not isinstance(self.about, OntologyElement):
            self.about = OntologyElement()

        super().__post_init__(**kwargs)


@dataclass
class NodeUnobsoletion(NodeChange):
    """
    unobsoletion of a node deprecates usage of that node. Rarely applied.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeUnobsoletion
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeUnobsoletion"
    class_name: ClassVar[str] = "node unobsoletion"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeUnobsoletion

    id: Union[str, NodeUnobsoletionId] = None
    change_description: Optional[str] = None
    replaced_by: Optional[Union[str, NodeId]] = None
    consider: Optional[Union[str, NodeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeUnobsoletionId):
            self.id = NodeUnobsoletionId(self.id)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        if self.replaced_by is not None and not isinstance(self.replaced_by, NodeId):
            self.replaced_by = NodeId(self.replaced_by)

        if self.consider is not None and not isinstance(self.consider, NodeId):
            self.consider = NodeId(self.consider)

        super().__post_init__(**kwargs)


@dataclass
class NodeCreation(NodeChange):
    """
    a node change in which a new node is created
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeCreation
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeCreation"
    class_name: ClassVar[str] = "node creation"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeCreation

    id: Union[str, NodeCreationId] = None
    node_id: Optional[Union[str, NodeId]] = None
    name: Optional[str] = None
    owl_type: Optional[Union[str, "OwlTypeEnum"]] = None
    annotation_set: Optional[Union[dict, "Annotation"]] = None
    language: Optional[str] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeCreationId):
            self.id = NodeCreationId(self.id)

        if self.node_id is not None and not isinstance(self.node_id, NodeId):
            self.node_id = NodeId(self.node_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.owl_type is not None and not isinstance(self.owl_type, OwlTypeEnum):
            self.owl_type = OwlTypeEnum(self.owl_type)

        if self.annotation_set is not None and not isinstance(self.annotation_set, Annotation):
            self.annotation_set = Annotation(**as_dict(self.annotation_set))

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class ClassCreation(NodeCreation):
    """
    A node creation where the owl type is 'class'
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.ClassCreation
    class_class_curie: ClassVar[str] = "kgcl_schema:ClassCreation"
    class_name: ClassVar[str] = "class creation"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.ClassCreation

    id: Union[str, ClassCreationId] = None
    superclass: Optional[Union[str, NodeId]] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClassCreationId):
            self.id = ClassCreationId(self.id)

        if self.superclass is not None and not isinstance(self.superclass, NodeId):
            self.superclass = NodeId(self.superclass)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class NodeDeletion(NodeChange):
    """
    Deletion of a node from the graph. Note it is recommended nodes are obsoleted and never merged, but this operation
    exists to represent deletions in ontologies, accidental or otherwise
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeDeletion
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeDeletion"
    class_name: ClassVar[str] = "node deletion"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeDeletion

    id: Union[str, NodeDeletionId] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeDeletionId):
            self.id = NodeDeletionId(self.id)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class NodeDirectMerge(NodeObsoletion):
    """
    An obsoletion change in which all metadata (including name/label) from the source node is deleted and added to the
    target node, and edges can automatically be rewired to point to the target node
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeDirectMerge
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeDirectMerge"
    class_name: ClassVar[str] = "node direct merge"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeDirectMerge

    id: Union[str, NodeDirectMergeId] = None
    has_direct_replacement: Union[str, NodeId] = None
    about_node: Optional[Union[str, NodeId]] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeDirectMergeId):
            self.id = NodeDirectMergeId(self.id)

        if self._is_empty(self.has_direct_replacement):
            self.MissingRequiredField("has_direct_replacement")
        if not isinstance(self.has_direct_replacement, NodeId):
            self.has_direct_replacement = NodeId(self.has_direct_replacement)

        if self.about_node is not None and not isinstance(self.about_node, NodeId):
            self.about_node = NodeId(self.about_node)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class NodeObsoletionWithDirectReplacement(NodeObsoletion):
    """
    An obsoletion change in which information from the obsoleted node is selectively copied to a single target, and
    edges can automatically be rewired to point to the target node
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeObsoletionWithDirectReplacement
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeObsoletionWithDirectReplacement"
    class_name: ClassVar[str] = "node obsoletion with direct replacement"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeObsoletionWithDirectReplacement

    id: Union[str, NodeObsoletionWithDirectReplacementId] = None
    has_direct_replacement: Union[str, NodeId] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeObsoletionWithDirectReplacementId):
            self.id = NodeObsoletionWithDirectReplacementId(self.id)

        if self._is_empty(self.has_direct_replacement):
            self.MissingRequiredField("has_direct_replacement")
        if not isinstance(self.has_direct_replacement, NodeId):
            self.has_direct_replacement = NodeId(self.has_direct_replacement)

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


@dataclass
class NodeObsoletionWithNoDirectReplacement(NodeObsoletion):
    """
    An obsoletion change in which there is no direct replacement
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeObsoletionWithNoDirectReplacement
    class_class_curie: ClassVar[str] = "kgcl_schema:NodeObsoletionWithNoDirectReplacement"
    class_name: ClassVar[str] = "node obsoletion with no direct replacement"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.NodeObsoletionWithNoDirectReplacement

    id: Union[str, NodeObsoletionWithNoDirectReplacementId] = None
    has_nondirect_replacement: Union[Union[str, NodeId], List[Union[str, NodeId]]] = None
    change_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeObsoletionWithNoDirectReplacementId):
            self.id = NodeObsoletionWithNoDirectReplacementId(self.id)

        if self._is_empty(self.has_nondirect_replacement):
            self.MissingRequiredField("has_nondirect_replacement")
        if not isinstance(self.has_nondirect_replacement, list):
            self.has_nondirect_replacement = [self.has_nondirect_replacement] if self.has_nondirect_replacement is not None else []
        self.has_nondirect_replacement = [v if isinstance(v, NodeId) else NodeId(v) for v in self.has_nondirect_replacement]

        if self.change_description is not None and not isinstance(self.change_description, str):
            self.change_description = str(self.change_description)

        super().__post_init__(**kwargs)


class TextualDiff(YAMLRoot):
    """
    A summarizing of a change on a piece of text. This could be rendered in a number of different ways
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.TextualDiff
    class_class_curie: ClassVar[str] = "kgcl_schema:TextualDiff"
    class_name: ClassVar[str] = "textual diff"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.TextualDiff


@dataclass
class Configuration(YAMLRoot):
    """
    The meaning of operations can be configured
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.Configuration
    class_class_curie: ClassVar[str] = "kgcl_schema:Configuration"
    class_name: ClassVar[str] = "configuration"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Configuration

    name_predicate: Optional[str] = None
    definition_predicate: Optional[str] = None
    main_synonym_predicate: Optional[str] = None
    synonym_predicates: Optional[str] = None
    creator_predicate: Optional[str] = None
    contributor_predicate: Optional[str] = None
    obsoletion_workflow: Optional[str] = None
    obsoletion_policy: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name_predicate is not None and not isinstance(self.name_predicate, str):
            self.name_predicate = str(self.name_predicate)

        if self.definition_predicate is not None and not isinstance(self.definition_predicate, str):
            self.definition_predicate = str(self.definition_predicate)

        if self.main_synonym_predicate is not None and not isinstance(self.main_synonym_predicate, str):
            self.main_synonym_predicate = str(self.main_synonym_predicate)

        if self.synonym_predicates is not None and not isinstance(self.synonym_predicates, str):
            self.synonym_predicates = str(self.synonym_predicates)

        if self.creator_predicate is not None and not isinstance(self.creator_predicate, str):
            self.creator_predicate = str(self.creator_predicate)

        if self.contributor_predicate is not None and not isinstance(self.contributor_predicate, str):
            self.contributor_predicate = str(self.contributor_predicate)

        if self.obsoletion_workflow is not None and not isinstance(self.obsoletion_workflow, str):
            self.obsoletion_workflow = str(self.obsoletion_workflow)

        if self.obsoletion_policy is not None and not isinstance(self.obsoletion_policy, str):
            self.obsoletion_policy = str(self.obsoletion_policy)

        super().__post_init__(**kwargs)


@dataclass
class Session(YAMLRoot):
    """
    A session consists of a set of change sets bundled with the activities that generated those change sets
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KGCL_SCHEMA.Session
    class_class_curie: ClassVar[str] = "kgcl_schema:Session"
    class_name: ClassVar[str] = "session"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Session

    change_set: Optional[Union[Dict[Union[str, ChangeId], Union[dict, Change]], List[Union[dict, Change]]]] = empty_dict()
    activity_set: Optional[Union[Dict[Union[str, ActivityId], Union[dict, "Activity"]], List[Union[dict, "Activity"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="change_set", slot_type=Change, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="activity_set", slot_type=Activity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


class OntologyElement(YAMLRoot):
    """
    Any component of an ontology or knowledge graph
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OM.OntologyElement
    class_class_curie: ClassVar[str] = "om:OntologyElement"
    class_name: ClassVar[str] = "ontology element"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.OntologyElement


@dataclass
class PropertyValue(OntologyElement):
    """
    a property-value pair
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OM.PropertyValue
    class_class_curie: ClassVar[str] = "om:PropertyValue"
    class_name: ClassVar[str] = "property value"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.PropertyValue

    property: Optional[Union[str, NodeId]] = None
    filler: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.property is not None and not isinstance(self.property, NodeId):
            self.property = NodeId(self.property)

        if self.filler is not None and not isinstance(self.filler, str):
            self.filler = str(self.filler)

        super().__post_init__(**kwargs)


@dataclass
class Annotation(PropertyValue):
    """
    owl annotations. Not to be confused with annotations sensu GO
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OM.Annotation
    class_class_curie: ClassVar[str] = "om:Annotation"
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Annotation

    property: Optional[Union[str, NodeId]] = None
    filler: Optional[str] = None
    annotation_set: Optional[Union[dict, "Annotation"]] = None
    property_type: Optional[str] = None
    filler_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.property is not None and not isinstance(self.property, NodeId):
            self.property = NodeId(self.property)

        if self.filler is not None and not isinstance(self.filler, str):
            self.filler = str(self.filler)

        if self.annotation_set is not None and not isinstance(self.annotation_set, Annotation):
            self.annotation_set = Annotation(**as_dict(self.annotation_set))

        if self.property_type is not None and not isinstance(self.property_type, str):
            self.property_type = str(self.property_type)

        if self.filler_type is not None and not isinstance(self.filler_type, str):
            self.filler_type = str(self.filler_type)

        super().__post_init__(**kwargs)


@dataclass
class Node(OntologyElement):
    """
    Any named entity in an ontology. May be a class, individual, property
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OM.Node
    class_class_curie: ClassVar[str] = "om:Node"
    class_name: ClassVar[str] = "node"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Node

    id: Union[str, NodeId] = None
    name: Optional[str] = None
    annotation_set: Optional[Union[dict, Annotation]] = None
    owl_type: Optional[Union[str, "OwlTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NodeId):
            self.id = NodeId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.annotation_set is not None and not isinstance(self.annotation_set, Annotation):
            self.annotation_set = Annotation(**as_dict(self.annotation_set))

        if self.owl_type is not None and not isinstance(self.owl_type, OwlTypeEnum):
            self.owl_type = OwlTypeEnum(self.owl_type)

        super().__post_init__(**kwargs)


@dataclass
class ClassNode(Node):
    """
    A node that is a class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Class
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "class node"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.ClassNode

    id: Union[str, ClassNodeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClassNodeId):
            self.id = ClassNodeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class InstanceNode(Node):
    """
    A node that is an individual
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.NamedIndividual
    class_class_curie: ClassVar[str] = "owl:NamedIndividual"
    class_name: ClassVar[str] = "instance node"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.InstanceNode

    id: Union[str, InstanceNodeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstanceNodeId):
            self.id = InstanceNodeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Edge(OntologyElement):
    """
    A relationship between two nodes.
    Currently the only kinds of edges supported in KGCL:

    * A subClassOf B <==> Edge(subject=A, predicate=owl:subClassOf, object=B)
    * A subClassOf P some B <==> Edge(subject=A, predicate=P, object=B)
    * P subPropertyOf Q <==> Edge(subject=P, predicate=owl:subPropertyOf, object=Q)

    These represent the most common kind of pairwise relationship between classes, and classes are the dominant node
    type in ontologies.

    In future a wider variety of OWL axiom types will be supportedn through the use of an additional edge
    property/slot to indicate the interpretation of the axiom, following owlstar
    (https://github.com/cmungall/owlstar).
    For example:
    * `A subClassOf R only B <==> Edge(subject=A, predicate=P, object=B, interpretation=AllOnly)`
    * `A Annotation(P,B) <==> Edge(subject=A, predicate=P, object=B, interpretation=annotationAssertion)`

    Note that not all axioms are intended to map to edges. Axioms/triples where the object is a literal would be
    represented as node properties. Complex OWL axioms involving nesting would have their own dedicated construct, or
    may be represented generically. These are out of scope for the current version of KGCL
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OM.Edge
    class_class_curie: ClassVar[str] = "om:Edge"
    class_name: ClassVar[str] = "edge"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Edge

    subject: Optional[Union[str, NodeId]] = None
    predicate: Optional[Union[str, NodeId]] = None
    object: Optional[Union[str, NodeId]] = None
    subject_representation: Optional[str] = None
    predicate_representation: Optional[str] = None
    object_representation: Optional[str] = None
    annotation_set: Optional[Union[dict, Annotation]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, NodeId):
            self.subject = NodeId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, NodeId):
            self.predicate = NodeId(self.predicate)

        if self.object is not None and not isinstance(self.object, NodeId):
            self.object = NodeId(self.object)

        if self.subject_representation is not None and not isinstance(self.subject_representation, str):
            self.subject_representation = str(self.subject_representation)

        if self.predicate_representation is not None and not isinstance(self.predicate_representation, str):
            self.predicate_representation = str(self.predicate_representation)

        if self.object_representation is not None and not isinstance(self.object_representation, str):
            self.object_representation = str(self.object_representation)

        if self.annotation_set is not None and not isinstance(self.annotation_set, Annotation):
            self.annotation_set = Annotation(**as_dict(self.annotation_set))

        super().__post_init__(**kwargs)


class LogicalDefinition(OntologyElement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OM.LogicalDefinition
    class_class_curie: ClassVar[str] = "om:LogicalDefinition"
    class_name: ClassVar[str] = "logical definition"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.LogicalDefinition


class OntologySubset(OntologyElement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OM.OntologySubset
    class_class_curie: ClassVar[str] = "om:OntologySubset"
    class_name: ClassVar[str] = "ontology subset"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.OntologySubset


@dataclass
class Activity(YAMLRoot):
    """
    a provence-generating activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Activity
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "activity"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Activity

    id: Union[str, ActivityId] = None
    started_at_time: Optional[str] = None
    ended_at_time: Optional[str] = None
    was_informed_by: Optional[Union[str, ActivityId]] = None
    was_associated_with: Optional[Union[str, AgentId]] = None
    used: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        if self.started_at_time is not None and not isinstance(self.started_at_time, str):
            self.started_at_time = str(self.started_at_time)

        if self.ended_at_time is not None and not isinstance(self.ended_at_time, str):
            self.ended_at_time = str(self.ended_at_time)

        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)

        if self.was_associated_with is not None and not isinstance(self.was_associated_with, AgentId):
            self.was_associated_with = AgentId(self.was_associated_with)

        if self.used is not None and not isinstance(self.used, str):
            self.used = str(self.used)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Agent(YAMLRoot):
    """
    a provence-generating agent
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Agent
    class_class_curie: ClassVar[str] = "prov:Agent"
    class_name: ClassVar[str] = "agent"
    class_model_uri: ClassVar[URIRef] = KGCL_SCHEMA.Agent

    id: Union[str, AgentId] = None
    acted_on_behalf_of: Optional[Union[str, AgentId]] = None
    was_informed_by: Optional[Union[str, ActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        if self.acted_on_behalf_of is not None and not isinstance(self.acted_on_behalf_of, AgentId):
            self.acted_on_behalf_of = AgentId(self.acted_on_behalf_of)

        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)

        super().__post_init__(**kwargs)


# Enumerations
class OwlTypeEnum(EnumDefinitionImpl):

    CLASS = PermissibleValue(text="CLASS",
                                 meaning=OWL.Class)
    OBJECT_PROPERTY = PermissibleValue(text="OBJECT_PROPERTY",
                                                     meaning=OWL.ObjectProperty)
    NAMED_INDIVIDUAL = PermissibleValue(text="NAMED_INDIVIDUAL",
                                                       meaning=OWL.NamedIndividual)

    _defn = EnumDefinition(
        name="OwlTypeEnum",
    )

class SynonymScopeEnum(EnumDefinitionImpl):

    related = PermissibleValue(text="related",
                                     meaning=OIO.hasNarrowSynonym)
    broad = PermissibleValue(text="broad",
                                 meaning=OIO.hasBroadSynonym)
    narrow = PermissibleValue(text="narrow",
                                   meaning=OIO.hasNarrowSynonym)
    exact = PermissibleValue(text="exact",
                                 meaning=OIO.hasExactSynonym)

    _defn = EnumDefinition(
        name="SynonymScopeEnum",
    )



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

# Slots
class slots:
    pass

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=KGCL_SCHEMA.type, domain=None, range=Optional[str])

slots.pull_request = Slot(uri=KGCL_SCHEMA.pull_request, name="pull request", curie=KGCL_SCHEMA.curie('pull_request'),
                   model_uri=KGCL_SCHEMA.pull_request, domain=None, range=Optional[str])

slots.see_also = Slot(uri=RDFS.seeAlso, name="see also", curie=RDFS.curie('seeAlso'),
                   model_uri=KGCL_SCHEMA.see_also, domain=None, range=Optional[str])

slots.creator = Slot(uri=DCTERMS.creator, name="creator", curie=DCTERMS.curie('creator'),
                   model_uri=KGCL_SCHEMA.creator, domain=None, range=Optional[str])

slots.contributor = Slot(uri=DCTERMS.creator, name="contributor", curie=DCTERMS.curie('creator'),
                   model_uri=KGCL_SCHEMA.contributor, domain=None, range=Optional[str])

slots.change_date = Slot(uri=DCTERMS.date, name="change date", curie=DCTERMS.curie('date'),
                   model_uri=KGCL_SCHEMA.change_date, domain=None, range=Optional[str])

slots.has_undo = Slot(uri=KGCL_SCHEMA.has_undo, name="has undo", curie=KGCL_SCHEMA.curie('has_undo'),
                   model_uri=KGCL_SCHEMA.has_undo, domain=Change, range=Optional[Union[str, ChangeId]])

slots.node_id = Slot(uri=KGCL_SCHEMA.node_id, name="node id", curie=KGCL_SCHEMA.curie('node_id'),
                   model_uri=KGCL_SCHEMA.node_id, domain=None, range=Optional[Union[str, NodeId]])

slots.superclass = Slot(uri=KGCL_SCHEMA.superclass, name="superclass", curie=KGCL_SCHEMA.curie('superclass'),
                   model_uri=KGCL_SCHEMA.superclass, domain=None, range=Optional[Union[str, NodeId]])

slots.language = Slot(uri=KGCL_SCHEMA.language, name="language", curie=KGCL_SCHEMA.curie('language'),
                   model_uri=KGCL_SCHEMA.language, domain=None, range=Optional[str])

slots.about = Slot(uri=KGCL_SCHEMA.about, name="about", curie=KGCL_SCHEMA.curie('about'),
                   model_uri=KGCL_SCHEMA.about, domain=None, range=Optional[Union[dict, OntologyElement]])

slots.about_node = Slot(uri=KGCL_SCHEMA.about_node, name="about node", curie=KGCL_SCHEMA.curie('about_node'),
                   model_uri=KGCL_SCHEMA.about_node, domain=None, range=Optional[Union[str, NodeId]])

slots.about_edge = Slot(uri=KGCL_SCHEMA.about_edge, name="about edge", curie=KGCL_SCHEMA.curie('about_edge'),
                   model_uri=KGCL_SCHEMA.about_edge, domain=None, range=Optional[Union[dict, Edge]])

slots.about_node_representation = Slot(uri=KGCL_SCHEMA.about_node_representation, name="about node representation", curie=KGCL_SCHEMA.curie('about_node_representation'),
                   model_uri=KGCL_SCHEMA.about_node_representation, domain=None, range=Optional[str])

slots.target = Slot(uri=KGCL_SCHEMA.target, name="target", curie=KGCL_SCHEMA.curie('target'),
                   model_uri=KGCL_SCHEMA.target, domain=None, range=Optional[str])

slots.old_value = Slot(uri=KGCL_SCHEMA.old_value, name="old value", curie=KGCL_SCHEMA.curie('old_value'),
                   model_uri=KGCL_SCHEMA.old_value, domain=None, range=Optional[str])

slots.new_value = Slot(uri=KGCL_SCHEMA.new_value, name="new value", curie=KGCL_SCHEMA.curie('new_value'),
                   model_uri=KGCL_SCHEMA.new_value, domain=None, range=Optional[str])

slots.datatype = Slot(uri=KGCL_SCHEMA.datatype, name="datatype", curie=KGCL_SCHEMA.curie('datatype'),
                   model_uri=KGCL_SCHEMA.datatype, domain=None, range=Optional[str])

slots.new_datatype = Slot(uri=KGCL_SCHEMA.new_datatype, name="new datatype", curie=KGCL_SCHEMA.curie('new_datatype'),
                   model_uri=KGCL_SCHEMA.new_datatype, domain=None, range=Optional[str])

slots.old_datatype = Slot(uri=KGCL_SCHEMA.old_datatype, name="old datatype", curie=KGCL_SCHEMA.curie('old_datatype'),
                   model_uri=KGCL_SCHEMA.old_datatype, domain=None, range=Optional[str])

slots.new_language = Slot(uri=KGCL_SCHEMA.new_language, name="new language", curie=KGCL_SCHEMA.curie('new_language'),
                   model_uri=KGCL_SCHEMA.new_language, domain=None, range=Optional[str])

slots.old_language = Slot(uri=KGCL_SCHEMA.old_language, name="old language", curie=KGCL_SCHEMA.curie('old_language'),
                   model_uri=KGCL_SCHEMA.old_language, domain=None, range=Optional[str])

slots.qualifier = Slot(uri=KGCL_SCHEMA.qualifier, name="qualifier", curie=KGCL_SCHEMA.curie('qualifier'),
                   model_uri=KGCL_SCHEMA.qualifier, domain=None, range=Optional[str])

slots.subclass = Slot(uri=KGCL_SCHEMA.subclass, name="subclass", curie=KGCL_SCHEMA.curie('subclass'),
                   model_uri=KGCL_SCHEMA.subclass, domain=None, range=Optional[str])

slots.new_subclass = Slot(uri=KGCL_SCHEMA.new_subclass, name="new subclass", curie=KGCL_SCHEMA.curie('new_subclass'),
                   model_uri=KGCL_SCHEMA.new_subclass, domain=None, range=Optional[str])

slots.new_property = Slot(uri=KGCL_SCHEMA.new_property, name="new property", curie=KGCL_SCHEMA.curie('new_property'),
                   model_uri=KGCL_SCHEMA.new_property, domain=None, range=Optional[str])

slots.new_filler = Slot(uri=KGCL_SCHEMA.new_filler, name="new filler", curie=KGCL_SCHEMA.curie('new_filler'),
                   model_uri=KGCL_SCHEMA.new_filler, domain=None, range=Optional[str])

slots.object_type = Slot(uri=KGCL_SCHEMA.object_type, name="object type", curie=KGCL_SCHEMA.curie('object_type'),
                   model_uri=KGCL_SCHEMA.object_type, domain=None, range=Optional[str])

slots.new_object_type = Slot(uri=KGCL_SCHEMA.new_object_type, name="new object type", curie=KGCL_SCHEMA.curie('new_object_type'),
                   model_uri=KGCL_SCHEMA.new_object_type, domain=None, range=Optional[str])

slots.old_object_type = Slot(uri=KGCL_SCHEMA.old_object_type, name="old object type", curie=KGCL_SCHEMA.curie('old_object_type'),
                   model_uri=KGCL_SCHEMA.old_object_type, domain=None, range=Optional[str])

slots.new_value_type = Slot(uri=KGCL_SCHEMA.new_value_type, name="new value type", curie=KGCL_SCHEMA.curie('new_value_type'),
                   model_uri=KGCL_SCHEMA.new_value_type, domain=None, range=Optional[str])

slots.old_value_type = Slot(uri=KGCL_SCHEMA.old_value_type, name="old value type", curie=KGCL_SCHEMA.curie('old_value_type'),
                   model_uri=KGCL_SCHEMA.old_value_type, domain=None, range=Optional[str])

slots.subject_type = Slot(uri=KGCL_SCHEMA.subject_type, name="subject type", curie=KGCL_SCHEMA.curie('subject_type'),
                   model_uri=KGCL_SCHEMA.subject_type, domain=None, range=Optional[str])

slots.subclass_type = Slot(uri=KGCL_SCHEMA.subclass_type, name="subclass type", curie=KGCL_SCHEMA.curie('subclass_type'),
                   model_uri=KGCL_SCHEMA.subclass_type, domain=None, range=Optional[str])

slots.superclass_type = Slot(uri=KGCL_SCHEMA.superclass_type, name="superclass type", curie=KGCL_SCHEMA.curie('superclass_type'),
                   model_uri=KGCL_SCHEMA.superclass_type, domain=None, range=Optional[str])

slots.predicate_type = Slot(uri=KGCL_SCHEMA.predicate_type, name="predicate type", curie=KGCL_SCHEMA.curie('predicate_type'),
                   model_uri=KGCL_SCHEMA.predicate_type, domain=None, range=Optional[str])

slots.in_subset = Slot(uri=KGCL_SCHEMA.in_subset, name="in subset", curie=KGCL_SCHEMA.curie('in_subset'),
                   model_uri=KGCL_SCHEMA.in_subset, domain=None, range=Optional[Union[dict, OntologySubset]])

slots.annotation_property = Slot(uri=KGCL_SCHEMA.annotation_property, name="annotation property", curie=KGCL_SCHEMA.curie('annotation_property'),
                   model_uri=KGCL_SCHEMA.annotation_property, domain=None, range=Optional[str])

slots.annotation_property_type = Slot(uri=KGCL_SCHEMA.annotation_property_type, name="annotation property type", curie=KGCL_SCHEMA.curie('annotation_property_type'),
                   model_uri=KGCL_SCHEMA.annotation_property_type, domain=None, range=Optional[str])

slots.change_description = Slot(uri=KGCL_SCHEMA.change_description, name="change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.change_description, domain=None, range=Optional[str])

slots.has_textual_diff = Slot(uri=KGCL_SCHEMA.has_textual_diff, name="has textual diff", curie=KGCL_SCHEMA.curie('has_textual_diff'),
                   model_uri=KGCL_SCHEMA.has_textual_diff, domain=Change, range=Optional[Union[dict, "TextualDiff"]])

slots.change_set = Slot(uri=KGCL_SCHEMA.change_set, name="change set", curie=KGCL_SCHEMA.curie('change_set'),
                   model_uri=KGCL_SCHEMA.change_set, domain=None, range=Optional[Union[Dict[Union[str, ChangeId], Union[dict, Change]], List[Union[dict, Change]]]])

slots.has_replacement = Slot(uri=KGCL_SCHEMA.has_replacement, name="has replacement", curie=KGCL_SCHEMA.curie('has_replacement'),
                   model_uri=KGCL_SCHEMA.has_replacement, domain=NodeObsoletion, range=Optional[Union[str, NodeId]])

slots.has_direct_replacement = Slot(uri=KGCL_SCHEMA.has_direct_replacement, name="has direct replacement", curie=KGCL_SCHEMA.curie('has_direct_replacement'),
                   model_uri=KGCL_SCHEMA.has_direct_replacement, domain=None, range=Optional[Union[str, NodeId]])

slots.has_nondirect_replacement = Slot(uri=KGCL_SCHEMA.has_nondirect_replacement, name="has nondirect replacement", curie=KGCL_SCHEMA.curie('has_nondirect_replacement'),
                   model_uri=KGCL_SCHEMA.has_nondirect_replacement, domain=None, range=Optional[Union[Union[str, NodeId], List[Union[str, NodeId]]]])

slots.owl_type = Slot(uri=OM.owl_type, name="owl type", curie=OM.curie('owl_type'),
                   model_uri=KGCL_SCHEMA.owl_type, domain=None, range=Optional[Union[str, "OwlTypeEnum"]])

slots.name = Slot(uri=OM.name, name="name", curie=OM.curie('name'),
                   model_uri=KGCL_SCHEMA.name, domain=None, range=Optional[str])

slots.subject = Slot(uri=OM.subject, name="subject", curie=OM.curie('subject'),
                   model_uri=KGCL_SCHEMA.subject, domain=None, range=Optional[Union[str, NodeId]])

slots.object = Slot(uri=OM.object, name="object", curie=OM.curie('object'),
                   model_uri=KGCL_SCHEMA.object, domain=None, range=Optional[Union[str, NodeId]])

slots.predicate = Slot(uri=OM.predicate, name="predicate", curie=OM.curie('predicate'),
                   model_uri=KGCL_SCHEMA.predicate, domain=None, range=Optional[Union[str, NodeId]])

slots.annotation_set = Slot(uri=OM.annotation_set, name="annotation set", curie=OM.curie('annotation_set'),
                   model_uri=KGCL_SCHEMA.annotation_set, domain=None, range=Optional[Union[dict, Annotation]])

slots.property = Slot(uri=OM.property, name="property", curie=OM.curie('property'),
                   model_uri=KGCL_SCHEMA.property, domain=None, range=Optional[Union[str, NodeId]])

slots.filler = Slot(uri=OM.filler, name="filler", curie=OM.curie('filler'),
                   model_uri=KGCL_SCHEMA.filler, domain=None, range=Optional[str])

slots.property_type = Slot(uri=OM.property_type, name="property type", curie=OM.curie('property_type'),
                   model_uri=KGCL_SCHEMA.property_type, domain=None, range=Optional[str])

slots.filler_type = Slot(uri=OM.filler_type, name="filler type", curie=OM.curie('filler_type'),
                   model_uri=KGCL_SCHEMA.filler_type, domain=None, range=Optional[str])

slots.subject_representation = Slot(uri=OM.subject_representation, name="subject representation", curie=OM.curie('subject_representation'),
                   model_uri=KGCL_SCHEMA.subject_representation, domain=None, range=Optional[str])

slots.predicate_representation = Slot(uri=OM.predicate_representation, name="predicate representation", curie=OM.curie('predicate_representation'),
                   model_uri=KGCL_SCHEMA.predicate_representation, domain=None, range=Optional[str])

slots.object_representation = Slot(uri=OM.object_representation, name="object representation", curie=OM.curie('object_representation'),
                   model_uri=KGCL_SCHEMA.object_representation, domain=None, range=Optional[str])

slots.property_value_set = Slot(uri=OM.property_value_set, name="property value set", curie=OM.curie('property_value_set'),
                   model_uri=KGCL_SCHEMA.property_value_set, domain=None, range=Optional[Union[Union[dict, PropertyValue], List[Union[dict, PropertyValue]]]])

slots.started_at_time = Slot(uri=PROV.startedAtTime, name="started at time", curie=PROV.curie('startedAtTime'),
                   model_uri=KGCL_SCHEMA.started_at_time, domain=None, range=Optional[str])

slots.ended_at_time = Slot(uri=PROV.endedAtTime, name="ended at time", curie=PROV.curie('endedAtTime'),
                   model_uri=KGCL_SCHEMA.ended_at_time, domain=None, range=Optional[str])

slots.was_informed_by = Slot(uri=PROV.wasInformedBy, name="was informed by", curie=PROV.curie('wasInformedBy'),
                   model_uri=KGCL_SCHEMA.was_informed_by, domain=None, range=Optional[Union[str, ActivityId]])

slots.was_associated_with = Slot(uri=PROV.wasAssociatedWith, name="was associated with", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=KGCL_SCHEMA.was_associated_with, domain=None, range=Optional[Union[str, AgentId]])

slots.acted_on_behalf_of = Slot(uri=PROV.actedOnBehalfOf, name="acted on behalf of", curie=PROV.curie('actedOnBehalfOf'),
                   model_uri=KGCL_SCHEMA.acted_on_behalf_of, domain=None, range=Optional[Union[str, AgentId]])

slots.was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="was generated by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=KGCL_SCHEMA.was_generated_by, domain=None, range=Optional[Union[str, ActivityId]])

slots.used = Slot(uri=PROV.used, name="used", curie=PROV.curie('used'),
                   model_uri=KGCL_SCHEMA.used, domain=Activity, range=Optional[str])

slots.activity_set = Slot(uri=PROV.activity_set, name="activity set", curie=PROV.curie('activity_set'),
                   model_uri=KGCL_SCHEMA.activity_set, domain=None, range=Optional[Union[Dict[Union[str, ActivityId], Union[dict, Activity]], List[Union[dict, Activity]]]])

slots.agent_set = Slot(uri=PROV.agent_set, name="agent set", curie=PROV.curie('agent_set'),
                   model_uri=KGCL_SCHEMA.agent_set, domain=None, range=Optional[Union[Dict[Union[str, AgentId], Union[dict, Agent]], List[Union[dict, Agent]]]])

slots.id = Slot(uri=BASICS.id, name="id", curie=BASICS.curie('id'),
                   model_uri=KGCL_SCHEMA.id, domain=None, range=URIRef)

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=KGCL_SCHEMA.description, domain=None, range=Optional[str])

slots.configuration__name_predicate = Slot(uri=KGCL_SCHEMA.name_predicate, name="configuration__name_predicate", curie=KGCL_SCHEMA.curie('name_predicate'),
                   model_uri=KGCL_SCHEMA.configuration__name_predicate, domain=None, range=Optional[str])

slots.configuration__definition_predicate = Slot(uri=KGCL_SCHEMA.definition_predicate, name="configuration__definition_predicate", curie=KGCL_SCHEMA.curie('definition_predicate'),
                   model_uri=KGCL_SCHEMA.configuration__definition_predicate, domain=None, range=Optional[str])

slots.configuration__main_synonym_predicate = Slot(uri=KGCL_SCHEMA.main_synonym_predicate, name="configuration__main_synonym_predicate", curie=KGCL_SCHEMA.curie('main_synonym_predicate'),
                   model_uri=KGCL_SCHEMA.configuration__main_synonym_predicate, domain=None, range=Optional[str])

slots.configuration__synonym_predicates = Slot(uri=KGCL_SCHEMA.synonym_predicates, name="configuration__synonym_predicates", curie=KGCL_SCHEMA.curie('synonym_predicates'),
                   model_uri=KGCL_SCHEMA.configuration__synonym_predicates, domain=None, range=Optional[str])

slots.configuration__creator_predicate = Slot(uri=KGCL_SCHEMA.creator_predicate, name="configuration__creator_predicate", curie=KGCL_SCHEMA.curie('creator_predicate'),
                   model_uri=KGCL_SCHEMA.configuration__creator_predicate, domain=None, range=Optional[str])

slots.configuration__contributor_predicate = Slot(uri=KGCL_SCHEMA.contributor_predicate, name="configuration__contributor_predicate", curie=KGCL_SCHEMA.curie('contributor_predicate'),
                   model_uri=KGCL_SCHEMA.configuration__contributor_predicate, domain=None, range=Optional[str])

slots.configuration__obsoletion_workflow = Slot(uri=KGCL_SCHEMA.obsoletion_workflow, name="configuration__obsoletion_workflow", curie=KGCL_SCHEMA.curie('obsoletion_workflow'),
                   model_uri=KGCL_SCHEMA.configuration__obsoletion_workflow, domain=None, range=Optional[str])

slots.configuration__obsoletion_policy = Slot(uri=KGCL_SCHEMA.obsoletion_policy, name="configuration__obsoletion_policy", curie=KGCL_SCHEMA.curie('obsoletion_policy'),
                   model_uri=KGCL_SCHEMA.configuration__obsoletion_policy, domain=None, range=Optional[str])

slots.associated_change_set = Slot(uri=KGCL_SCHEMA.associated_change_set, name="associated change set", curie=KGCL_SCHEMA.curie('associated_change_set'),
                   model_uri=KGCL_SCHEMA.associated_change_set, domain=None, range=Optional[Union[Dict[Union[str, ChangeId], Union[dict, Change]], List[Union[dict, Change]]]])

slots.change_type = Slot(uri=KGCL_SCHEMA.change_type, name="change type", curie=KGCL_SCHEMA.curie('change_type'),
                   model_uri=KGCL_SCHEMA.change_type, domain=None, range=Optional[Union[str, ChangeClassType]])

slots.count = Slot(uri=KGCL_SCHEMA.count, name="count", curie=KGCL_SCHEMA.curie('count'),
                   model_uri=KGCL_SCHEMA.count, domain=None, range=Optional[int])

slots.change_1 = Slot(uri=KGCL_SCHEMA.change_1, name="change 1", curie=KGCL_SCHEMA.curie('change_1'),
                   model_uri=KGCL_SCHEMA.change_1, domain=None, range=Optional[Union[str, NodeRenameId]])

slots.change_2 = Slot(uri=KGCL_SCHEMA.change_2, name="change 2", curie=KGCL_SCHEMA.curie('change_2'),
                   model_uri=KGCL_SCHEMA.change_2, domain=None, range=Optional[Union[str, NewSynonymId]])

slots.subset = Slot(uri=KGCL_SCHEMA.subset, name="subset", curie=KGCL_SCHEMA.curie('subset'),
                   model_uri=KGCL_SCHEMA.subset, domain=None, range=Optional[str])

slots.replaced_by = Slot(uri=KGCL_SCHEMA.replaced_by, name="replaced by", curie=KGCL_SCHEMA.curie('replaced_by'),
                   model_uri=KGCL_SCHEMA.replaced_by, domain=None, range=Optional[Union[str, NodeId]])

slots.consider = Slot(uri=KGCL_SCHEMA.consider, name="consider", curie=KGCL_SCHEMA.curie('consider'),
                   model_uri=KGCL_SCHEMA.consider, domain=None, range=Optional[Union[str, NodeId]])

slots.change_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="change_was generated by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=KGCL_SCHEMA.change_was_generated_by, domain=Change, range=Optional[Union[str, ActivityId]])

slots.change_see_also = Slot(uri=RDFS.seeAlso, name="change_see also", curie=RDFS.curie('seeAlso'),
                   model_uri=KGCL_SCHEMA.change_see_also, domain=Change, range=Optional[str])

slots.change_pull_request = Slot(uri=KGCL_SCHEMA.pull_request, name="change_pull request", curie=KGCL_SCHEMA.curie('pull_request'),
                   model_uri=KGCL_SCHEMA.change_pull_request, domain=Change, range=Optional[str])

slots.change_creator = Slot(uri=DCTERMS.creator, name="change_creator", curie=DCTERMS.curie('creator'),
                   model_uri=KGCL_SCHEMA.change_creator, domain=Change, range=Optional[str])

slots.change_change_date = Slot(uri=DCTERMS.date, name="change_change date", curie=DCTERMS.curie('date'),
                   model_uri=KGCL_SCHEMA.change_change_date, domain=Change, range=Optional[str])

slots.multi_node_obsoletion_change_set = Slot(uri=KGCL_SCHEMA.change_set, name="multi node obsoletion_change set", curie=KGCL_SCHEMA.curie('change_set'),
                   model_uri=KGCL_SCHEMA.multi_node_obsoletion_change_set, domain=MultiNodeObsoletion, range=Optional[Union[Dict[Union[str, NodeObsoletionId], Union[dict, "NodeObsoletion"]], List[Union[dict, "NodeObsoletion"]]]])

slots.multi_node_obsoletion_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="multi node obsoletion_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.multi_node_obsoletion_change_description, domain=MultiNodeObsoletion, range=Optional[str])

slots.multi_node_obsoletion_associated_change_set = Slot(uri=KGCL_SCHEMA.associated_change_set, name="multi node obsoletion_associated change set", curie=KGCL_SCHEMA.curie('associated_change_set'),
                   model_uri=KGCL_SCHEMA.multi_node_obsoletion_associated_change_set, domain=MultiNodeObsoletion, range=Optional[Union[Dict[Union[str, ChangeId], Union[dict, Change]], List[Union[dict, Change]]]])

slots.change_set_summary_statistic_change_type = Slot(uri=KGCL_SCHEMA.change_type, name="change set summary statistic_change type", curie=KGCL_SCHEMA.curie('change_type'),
                   model_uri=KGCL_SCHEMA.change_set_summary_statistic_change_type, domain=ChangeSetSummaryStatistic, range=Optional[Union[str, ChangeClassType]])

slots.change_set_summary_statistic_count = Slot(uri=KGCL_SCHEMA.count, name="change set summary statistic_count", curie=KGCL_SCHEMA.curie('count'),
                   model_uri=KGCL_SCHEMA.change_set_summary_statistic_count, domain=ChangeSetSummaryStatistic, range=Optional[int])

slots.change_set_summary_statistic_property_value_set = Slot(uri=OM.property_value_set, name="change set summary statistic_property value set", curie=OM.curie('property_value_set'),
                   model_uri=KGCL_SCHEMA.change_set_summary_statistic_property_value_set, domain=ChangeSetSummaryStatistic, range=Optional[Union[Union[dict, "PropertyValue"], List[Union[dict, "PropertyValue"]]]])

slots.obsoletion_about = Slot(uri=KGCL_SCHEMA.about, name="obsoletion_about", curie=KGCL_SCHEMA.curie('about'),
                   model_uri=KGCL_SCHEMA.obsoletion_about, domain=None, range=Optional[Union[dict, "OntologyElement"]])

slots.obsoletion_has_undo = Slot(uri=KGCL_SCHEMA.has_undo, name="obsoletion_has undo", curie=KGCL_SCHEMA.curie('has_undo'),
                   model_uri=KGCL_SCHEMA.obsoletion_has_undo, domain=None, range=Optional[Union[dict, "Obsoletion"]])

slots.language_tag_change_old_value = Slot(uri=KGCL_SCHEMA.old_value, name="language tag change_old value", curie=KGCL_SCHEMA.curie('old_value'),
                   model_uri=KGCL_SCHEMA.language_tag_change_old_value, domain=LanguageTagChange, range=Optional[str])

slots.language_tag_change_new_value = Slot(uri=KGCL_SCHEMA.new_value, name="language tag change_new value", curie=KGCL_SCHEMA.curie('new_value'),
                   model_uri=KGCL_SCHEMA.language_tag_change_new_value, domain=LanguageTagChange, range=Optional[str])

slots.unobsoletion_has_undo = Slot(uri=KGCL_SCHEMA.has_undo, name="unobsoletion_has undo", curie=KGCL_SCHEMA.curie('has_undo'),
                   model_uri=KGCL_SCHEMA.unobsoletion_has_undo, domain=None, range=Optional[Union[dict, Obsoletion]])

slots.creation_has_undo = Slot(uri=KGCL_SCHEMA.has_undo, name="creation_has undo", curie=KGCL_SCHEMA.curie('has_undo'),
                   model_uri=KGCL_SCHEMA.creation_has_undo, domain=None, range=Optional[Union[dict, Deletion]])

slots.add_to_subset_in_subset = Slot(uri=KGCL_SCHEMA.in_subset, name="add to subset_in subset", curie=KGCL_SCHEMA.curie('in_subset'),
                   model_uri=KGCL_SCHEMA.add_to_subset_in_subset, domain=None, range=Optional[Union[dict, "OntologySubset"]])

slots.remove_from_subset_in_subset = Slot(uri=KGCL_SCHEMA.in_subset, name="remove from subset_in subset", curie=KGCL_SCHEMA.curie('in_subset'),
                   model_uri=KGCL_SCHEMA.remove_from_subset_in_subset, domain=None, range=Optional[Union[dict, "OntologySubset"]])

slots.remove_from_subset_has_undo = Slot(uri=KGCL_SCHEMA.has_undo, name="remove from subset_has undo", curie=KGCL_SCHEMA.curie('has_undo'),
                   model_uri=KGCL_SCHEMA.remove_from_subset_has_undo, domain=None, range=Optional[Union[dict, AddToSubset]])

slots.edge_change_subject = Slot(uri=OM.subject, name="edge change_subject", curie=OM.curie('subject'),
                   model_uri=KGCL_SCHEMA.edge_change_subject, domain=EdgeChange, range=Optional[Union[str, NodeId]])

slots.edge_creation_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="edge creation_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.edge_creation_change_description, domain=EdgeCreation, range=Optional[str])

slots.edge_deletion_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="edge deletion_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.edge_deletion_change_description, domain=EdgeDeletion, range=Optional[str])

slots.edge_obsoletion_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="edge obsoletion_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.edge_obsoletion_change_description, domain=EdgeObsoletion, range=Optional[str])

slots.mapping_creation_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="mapping creation_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.mapping_creation_change_description, domain=MappingCreation, range=Optional[str])

slots.mapping_creation_subject = Slot(uri=OM.subject, name="mapping creation_subject", curie=OM.curie('subject'),
                   model_uri=KGCL_SCHEMA.mapping_creation_subject, domain=MappingCreation, range=Optional[Union[str, NodeId]])

slots.mapping_creation_predicate = Slot(uri=OM.predicate, name="mapping creation_predicate", curie=OM.curie('predicate'),
                   model_uri=KGCL_SCHEMA.mapping_creation_predicate, domain=MappingCreation, range=Optional[Union[str, NodeId]])

slots.mapping_creation_object = Slot(uri=OM.object, name="mapping creation_object", curie=OM.curie('object'),
                   model_uri=KGCL_SCHEMA.mapping_creation_object, domain=MappingCreation, range=Optional[Union[str, NodeId]])

slots.node_move_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="node move_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.node_move_change_description, domain=NodeMove, range=Optional[str])

slots.node_deepening_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="node deepening_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.node_deepening_change_description, domain=NodeDeepening, range=Optional[str])

slots.node_shallowing_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="node shallowing_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.node_shallowing_change_description, domain=NodeShallowing, range=Optional[str])

slots.predicate_change_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="predicate change_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.predicate_change_change_description, domain=PredicateChange, range=Optional[str])

slots.node_rename_old_value = Slot(uri=KGCL_SCHEMA.old_value, name="node rename_old value", curie=KGCL_SCHEMA.curie('old_value'),
                   model_uri=KGCL_SCHEMA.node_rename_old_value, domain=NodeRename, range=Optional[str])

slots.node_rename_new_value = Slot(uri=KGCL_SCHEMA.new_value, name="node rename_new value", curie=KGCL_SCHEMA.curie('new_value'),
                   model_uri=KGCL_SCHEMA.node_rename_new_value, domain=NodeRename, range=Optional[str])

slots.node_rename_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="node rename_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.node_rename_change_description, domain=NodeRename, range=Optional[str])

slots.set_language_for_name_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="set language for name_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.set_language_for_name_change_description, domain=SetLanguageForName, range=Optional[str])

slots.name_becomes_synonym_change_1 = Slot(uri=KGCL_SCHEMA.change_1, name="name becomes synonym_change 1", curie=KGCL_SCHEMA.curie('change_1'),
                   model_uri=KGCL_SCHEMA.name_becomes_synonym_change_1, domain=NameBecomesSynonym, range=Optional[Union[str, NodeRenameId]])

slots.name_becomes_synonym_change_2 = Slot(uri=KGCL_SCHEMA.change_2, name="name becomes synonym_change 2", curie=KGCL_SCHEMA.curie('change_2'),
                   model_uri=KGCL_SCHEMA.name_becomes_synonym_change_2, domain=NameBecomesSynonym, range=Optional[Union[str, NewSynonymId]])

slots.name_becomes_synonym_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="name becomes synonym_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.name_becomes_synonym_change_description, domain=NameBecomesSynonym, range=Optional[str])

slots.removed_node_from_subset_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="removed node from subset_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.removed_node_from_subset_change_description, domain=RemovedNodeFromSubset, range=Optional[str])

slots.removed_node_from_subset_about_node = Slot(uri=KGCL_SCHEMA.about_node, name="removed node from subset_about node", curie=KGCL_SCHEMA.curie('about_node'),
                   model_uri=KGCL_SCHEMA.removed_node_from_subset_about_node, domain=RemovedNodeFromSubset, range=Optional[Union[str, NodeId]])

slots.removed_node_from_subset_subset = Slot(uri=KGCL_SCHEMA.subset, name="removed node from subset_subset", curie=KGCL_SCHEMA.curie('subset'),
                   model_uri=KGCL_SCHEMA.removed_node_from_subset_subset, domain=RemovedNodeFromSubset, range=Optional[str])

slots.node_obsoletion_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="node obsoletion_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.node_obsoletion_change_description, domain=NodeObsoletion, range=Optional[str])

slots.node_obsoletion_associated_change_set = Slot(uri=KGCL_SCHEMA.associated_change_set, name="node obsoletion_associated change set", curie=KGCL_SCHEMA.curie('associated_change_set'),
                   model_uri=KGCL_SCHEMA.node_obsoletion_associated_change_set, domain=NodeObsoletion, range=Optional[Union[Dict[Union[str, ChangeId], Union[dict, Change]], List[Union[dict, Change]]]])

slots.node_unobsoletion_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="node unobsoletion_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.node_unobsoletion_change_description, domain=NodeUnobsoletion, range=Optional[str])

slots.node_unobsoletion_replaced_by = Slot(uri=KGCL_SCHEMA.replaced_by, name="node unobsoletion_replaced by", curie=KGCL_SCHEMA.curie('replaced_by'),
                   model_uri=KGCL_SCHEMA.node_unobsoletion_replaced_by, domain=NodeUnobsoletion, range=Optional[Union[str, NodeId]])

slots.node_unobsoletion_consider = Slot(uri=KGCL_SCHEMA.consider, name="node unobsoletion_consider", curie=KGCL_SCHEMA.curie('consider'),
                   model_uri=KGCL_SCHEMA.node_unobsoletion_consider, domain=NodeUnobsoletion, range=Optional[Union[str, NodeId]])

slots.node_creation_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="node creation_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.node_creation_change_description, domain=NodeCreation, range=Optional[str])

slots.class_creation_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="class creation_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.class_creation_change_description, domain=ClassCreation, range=Optional[str])

slots.node_deletion_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="node deletion_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.node_deletion_change_description, domain=NodeDeletion, range=Optional[str])

slots.node_direct_merge_has_direct_replacement = Slot(uri=KGCL_SCHEMA.has_direct_replacement, name="node direct merge_has direct replacement", curie=KGCL_SCHEMA.curie('has_direct_replacement'),
                   model_uri=KGCL_SCHEMA.node_direct_merge_has_direct_replacement, domain=NodeDirectMerge, range=Union[str, NodeId])

slots.node_direct_merge_about_node = Slot(uri=KGCL_SCHEMA.about_node, name="node direct merge_about node", curie=KGCL_SCHEMA.curie('about_node'),
                   model_uri=KGCL_SCHEMA.node_direct_merge_about_node, domain=NodeDirectMerge, range=Optional[Union[str, NodeId]])

slots.node_direct_merge_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="node direct merge_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.node_direct_merge_change_description, domain=NodeDirectMerge, range=Optional[str])

slots.node_obsoletion_with_direct_replacement_has_direct_replacement = Slot(uri=KGCL_SCHEMA.has_direct_replacement, name="node obsoletion with direct replacement_has direct replacement", curie=KGCL_SCHEMA.curie('has_direct_replacement'),
                   model_uri=KGCL_SCHEMA.node_obsoletion_with_direct_replacement_has_direct_replacement, domain=NodeObsoletionWithDirectReplacement, range=Union[str, NodeId])

slots.node_obsoletion_with_direct_replacement_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="node obsoletion with direct replacement_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.node_obsoletion_with_direct_replacement_change_description, domain=NodeObsoletionWithDirectReplacement, range=Optional[str])

slots.node_obsoletion_with_no_direct_replacement_has_nondirect_replacement = Slot(uri=KGCL_SCHEMA.has_nondirect_replacement, name="node obsoletion with no direct replacement_has nondirect replacement", curie=KGCL_SCHEMA.curie('has_nondirect_replacement'),
                   model_uri=KGCL_SCHEMA.node_obsoletion_with_no_direct_replacement_has_nondirect_replacement, domain=NodeObsoletionWithNoDirectReplacement, range=Union[Union[str, NodeId], List[Union[str, NodeId]]])

slots.node_obsoletion_with_no_direct_replacement_change_description = Slot(uri=KGCL_SCHEMA.change_description, name="node obsoletion with no direct replacement_change description", curie=KGCL_SCHEMA.curie('change_description'),
                   model_uri=KGCL_SCHEMA.node_obsoletion_with_no_direct_replacement_change_description, domain=NodeObsoletionWithNoDirectReplacement, range=Optional[str])