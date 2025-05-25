# kgcl-schema

A linkml based schema for Knowledge Graph Change Language (KGCL).
A data model for describing change operations at a high level on an
ontology or ontology-like artefact, such as a Knowledge Graph.

URI: https://w3id.org/hrshdhgd/kgcl-schema
Name: kgcl-schema

## Classes

| Class | Description |
| --- | --- |
| [Activity](Activity.md) | a provence-generating activity |
| [AddNodeToSubset](AddNodeToSubset.md) | Places a node inside a subset, by annotating that node |
| [AddToSubset](AddToSubset.md) | placing an element inside a subset |
| [Agent](Agent.md) | a provence-generating agent |
| [AllowsAutomaticReplacementOfEdges](AllowsAutomaticReplacementOfEdges.md) | Applies to an obsoletion in which annotations or edges pointing at the obsole... |
| [Annotation](Annotation.md) | owl annotations |
| [Change](Change.md) | Any change perform on an ontology or knowledge graph |
| [ChangeMixin](ChangeMixin.md) | root class for all change mixins |
| [ChangeSetSummaryStatistic](ChangeSetSummaryStatistic.md) | A summary statistic for a set of changes of the same type, grouped by zero or... |
| [ClassCreation](ClassCreation.md) | A node creation where the owl type is 'class' |
| [ClassNode](ClassNode.md) | A node that is a class |
| [ComplexChange](ComplexChange.md) | A change that is is a composition of other changes |
| [Configuration](Configuration.md) | The meaning of operations can be configured |
| [Creation](Creation.md) | Creation of an element |
| [DatatypeChange](DatatypeChange.md) |  |
| [DatatypeOrLanguageTagChange](DatatypeOrLanguageTagChange.md) | A change in a value assertion where the value remain unchanged but either the... |
| [Deletion](Deletion.md) | Removal of an element |
| [Edge](Edge.md) | A relationship between two nodes |
| [EdgeChange](EdgeChange.md) | A change in which the element that is the focus of the change is an edge |
| [EdgeCreation](EdgeCreation.md) | An edge change in which a de-novo edge is created |
| [EdgeDeletion](EdgeDeletion.md) | An edge change in which an edge is removed |
| [EdgeLogicalInterpretationChange](EdgeLogicalInterpretationChange.md) | An edge change where the subjet, object, and predicate are unchanged, but the... |
| [EdgeObsoletion](EdgeObsoletion.md) | An edge change in which an edge is obsoleted |
| [EdgeRewiring](EdgeRewiring.md) | An edge change where one node is replaced with another, as in the case of obs... |
| [InstanceNode](InstanceNode.md) | A node that is an individual |
| [LanguageTagChange](LanguageTagChange.md) |  |
| [LogicalAxiomChange](LogicalAxiomChange.md) | A simple change where a logical axiom is changed, where the logical axiom can... |
| [LogicalDefinition](LogicalDefinition.md) |  |
| [MappingCreation](MappingCreation.md) | A specific kind of edge creation in which the created edge is a mapping |
| [MultiNodeObsoletion](MultiNodeObsoletion.md) | A complex change consisting of multiple obsoletions |
| [NameBecomesSynonym](NameBecomesSynonym.md) | A node synonym where the name NAME of an node NODE moves to a synonym, and NO... |
| [NewSynonym](NewSynonym.md) | A node synonym change where a de-novo synonym is created |
| [NewTextDefinition](NewTextDefinition.md) | A node change where a de-novo text definition is created |
| [Node](Node.md) | Any named entity in an ontology |
| [NodeAnnotationChange](NodeAnnotationChange.md) | A node change where the change alters node properties/annotations |
| [NodeAnnotationReplacement](NodeAnnotationReplacement.md) | A node annotation change where the change replaces a particular property valu... |
| [NodeChange](NodeChange.md) | A simple change where the change is about a node |
| [NodeCreation](NodeCreation.md) | a node change in which a new node is created |
| [NodeDeepening](NodeDeepening.md) | A node move in which a node where the destination is a proper descendant of t... |
| [NodeDeletion](NodeDeletion.md) | Deletion of a node from the graph |
| [NodeDirectMerge](NodeDirectMerge.md) | An obsoletion change in which all metadata (including name/label) from the so... |
| [NodeMove](NodeMove.md) | A node move is a combination of deleting a parent edge and adding a parent ed... |
| [NodeObsoletion](NodeObsoletion.md) | Obsoletion of a node deprecates usage of that node, but does not delete it |
| [NodeObsoletionWithDirectReplacement](NodeObsoletionWithDirectReplacement.md) | An obsoletion change in which information from the obsoleted node is selectiv... |
| [NodeObsoletionWithNoDirectReplacement](NodeObsoletionWithNoDirectReplacement.md) | An obsoletion change in which there is no direct replacement |
| [NodeRename](NodeRename.md) | A node change where the name (aka rdfs:label) of the node changes |
| [NodeShallowing](NodeShallowing.md) | The opposite of node deepening |
| [NodeSynonymChange](NodeSynonymChange.md) |  |
| [NodeTextDefinitionChange](NodeTextDefinitionChange.md) | A node change where the text definition is changed |
| [NodeUnobsoletion](NodeUnobsoletion.md) | unobsoletion of a node deprecates usage of that node |
| [Obsoletion](Obsoletion.md) | Obsoletion of an element deprecates usage of that element, but does not delet... |
| [OntologyElement](OntologyElement.md) | Any component of an ontology or knowledge graph |
| [OntologySubset](OntologySubset.md) |  |
| [PlaceUnder](PlaceUnder.md) | An edge creation where the predicate is owl:subClassOf |
| [PredicateChange](PredicateChange.md) | An edge change where the predicate (relationship type) is modified |
| [PropertyValue](PropertyValue.md) | a property-value pair |
| [RemoveFromSubset](RemoveFromSubset.md) | removing an element from a subset |
| [RemoveSynonym](RemoveSynonym.md) | A node synonym change where a synonym is deleted |
| [RemoveTextDefinition](RemoveTextDefinition.md) | A node change where a text definition is deleted |
| [RemoveUnder](RemoveUnder.md) | An edge deletion where the predicate is owl:subClassOf |
| [RemovedNodeFromSubset](RemovedNodeFromSubset.md) | Removes a node from a subset, by removing an annotation |
| [Session](Session.md) | A session consists of a set of change sets bundled with the activities that g... |
| [SetLanguageForName](SetLanguageForName.md) | A node change where the string value for the name is unchanged but the langua... |
| [SimpleChange](SimpleChange.md) | A change that is about a single ontology element |
| [SubsetMembershipChange](SubsetMembershipChange.md) | A change in the membership status of a node with respect to a subset (view) |
| [SynonymPredicateChange](SynonymPredicateChange.md) | A node synonym change where the predicate of a synonym is changed |
| [SynonymReplacement](SynonymReplacement.md) | A node synonym change where the text of a synonym is changed |
| [TextDefinitionReplacement](TextDefinitionReplacement.md) | A node change where a text definition is modified |
| [TextualDiff](TextualDiff.md) | A summarizing of a change on a piece of text |
| [Transaction](Transaction.md) | A change that is a composition of a set of changes, where those changes are t... |
| [Unobsoletion](Unobsoletion.md) | Opposite operation of obsoletion |


## Slots

| Slot | Description |
| --- | --- |
| [about](about.md) | The 'focus' entity on which the change operates |
| [about_edge](about_edge.md) |  |
| [about_node](about_node.md) |  |
| [about_node_representation](about_node_representation.md) | The representation of a node (URI, CURIE, label)  |
| [acted_on_behalf_of](acted_on_behalf_of.md) |  |
| [activity_set](activity_set.md) |  |
| [agent_set](agent_set.md) |  |
| [annotation_property](annotation_property.md) | An annotation property |
| [annotation_property_type](annotation_property_type.md) | The type of a property (URI, CURIE, label)  |
| [annotation_set](annotation_set.md) |  |
| [change_date](change_date.md) |  |
| [change_description](change_description.md) | A string serialization of the change |
| [change_set](change_set.md) | A collection of changes |
| [contributor](contributor.md) |  |
| [contributor_predicate](contributor_predicate.md) |  |
| [creator](creator.md) |  |
| [creator_predicate](creator_predicate.md) |  |
| [datatype](datatype.md) | The datatype of a literal |
| [definition_predicate](definition_predicate.md) |  |
| [description](description.md) |  |
| [ended_at_time](ended_at_time.md) |  |
| [filler](filler.md) |  |
| [filler_type](filler_type.md) |  |
| [has_direct_replacement](has_direct_replacement.md) | An obsoletion replacement where it IS valid to automatically update annotatio... |
| [has_nondirect_replacement](has_nondirect_replacement.md) | An obsoletion replacement where it is NOT valid to automatically update annot... |
| [has_replacement](has_replacement.md) | A single node obsoletion event may be accompanied by one or more suggested re... |
| [has_textual_diff](has_textual_diff.md) | A representation of character-level changes on a textual literal property |
| [has_undo](has_undo.md) | A change that reverses this change |
| [id](id.md) |  |
| [in_subset](in_subset.md) | The subset that pertains to this change |
| [language](language.md) | The language tag of a literal |
| [main_synonym_predicate](main_synonym_predicate.md) |  |
| [name](name.md) |  |
| [name_predicate](name_predicate.md) |  |
| [new_datatype](new_datatype.md) | The new datatype of a literal |
| [new_filler](new_filler.md) | The new filler of an OWL restriction |
| [new_language](new_language.md) | The new language tag of a literal |
| [new_object_type](new_object_type.md) | The type (IRI or Literal) of a new object |
| [new_property](new_property.md) | The new property of an OWL restriction |
| [new_subclass](new_subclass.md) | The new subclass of a subsumption axiom |
| [new_value](new_value.md) | The value of a property held in the new instance of the ontology |
| [new_value_type](new_value_type.md) | The type (IRI or Literal) of a new value |
| [node_id](node_id.md) | id of a node to be created |
| [object](object.md) |  |
| [object_representation](object_representation.md) |  |
| [object_type](object_type.md) | The type (IRI or Literal) of an object |
| [obsoletion_policy](obsoletion_policy.md) |  |
| [obsoletion_workflow](obsoletion_workflow.md) |  |
| [old_datatype](old_datatype.md) | The old datatype of a literal |
| [old_language](old_language.md) | The old language tag of a literal |
| [old_object_type](old_object_type.md) | The type (IRI or Literal) of an old object |
| [old_value](old_value.md) | The value of a property held in the old instance of the ontology |
| [old_value_type](old_value_type.md) | The type (IRI or Literal) of an old value |
| [owl_type](owl_type.md) |  |
| [predicate](predicate.md) |  |
| [predicate_representation](predicate_representation.md) |  |
| [predicate_type](predicate_type.md) | The type (IRI or Literal) of an edge's subject |
| [property](property.md) |  |
| [property_type](property_type.md) |  |
| [property_value_set](property_value_set.md) |  |
| [pull_request](pull_request.md) |  |
| [qualifier](qualifier.md) | The qualifier of a change operation |
| [see_also](see_also.md) |  |
| [started_at_time](started_at_time.md) |  |
| [subclass](subclass.md) | The subclass of a subsumption axiom |
| [subclass_type](subclass_type.md) | The type of a subclass |
| [subject](subject.md) |  |
| [subject_representation](subject_representation.md) |  |
| [subject_type](subject_type.md) | The type (IRI or Literal) of an edge's subject |
| [superclass](superclass.md) |  |
| [superclass_type](superclass_type.md) | The type of a superclass |
| [synonym_predicates](synonym_predicates.md) |  |
| [target](target.md) | The secondary entity on which the change operates |
| [type](type.md) |  |
| [used](used.md) |  |
| [was_associated_with](was_associated_with.md) |  |
| [was_generated_by](was_generated_by.md) |  |
| [was_informed_by](was_informed_by.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [OwlTypeEnum](OwlTypeEnum.md) |  |
| [SynonymScopeEnum](SynonymScopeEnum.md) |  |


## Types

| Type | Description |
| --- | --- |
| [xsd:boolean](xsd:boolean) | A binary (true or false) value |
| [ChangeClassType](ChangeClassType.md) | CURIE for a class within this datamodel |
| [xsd:date](xsd:date) | a date (year, month and day) in an idealized calendar |
| [linkml:DateOrDatetime](https://w3id.org/linkml/DateOrDatetime) | Either a date or a datetime |
| [xsd:dateTime](xsd:dateTime) | The combination of a date and time |
| [xsd:decimal](xsd:decimal) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [xsd:double](xsd:double) | A real number that conforms to the xsd:double specification |
| [xsd:float](xsd:float) | A real number that conforms to the xsd:float specification |
| [xsd:integer](xsd:integer) | An integer |
| [LanguageTag](LanguageTag.md) |  |
| [xsd:string](xsd:string) | Prefix part of CURIE |
| [shex:nonLiteral](shex:nonLiteral) | A URI, CURIE or BNODE that represents a node in a model |
| [shex:iri](shex:iri) | A URI or CURIE that represents an object in the model |
| [xsd:string](xsd:string) | A character string |
| [xsd:dateTime](xsd:dateTime) | A time object represents a (local) time of day, independent of any particular... |
| [xsd:anyURI](xsd:anyURI) | a complete URI |
| [xsd:anyURI](xsd:anyURI) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
