# Class: EdgeObsoletion
_An edge change in which an edge is obsoleted._





URI: [kgcl_schema:EdgeObsoletion](https://w3id.org/kgcl-schema/EdgeObsoletion)




```mermaid
 classDiagram
      Obsoletion <|-- EdgeObsoletion
      EdgeChange <|-- EdgeObsoletion
      
      EdgeObsoletion : about_edge
      EdgeObsoletion : annotation_set
      EdgeObsoletion : change_date
      EdgeObsoletion : contributor
      EdgeObsoletion : creator
      EdgeObsoletion : datatype
      EdgeObsoletion : has_undo
      EdgeObsoletion : id
      EdgeObsoletion : language
      EdgeObsoletion : new_datatype
      EdgeObsoletion : new_language
      EdgeObsoletion : new_value
      EdgeObsoletion : new_value_type
      EdgeObsoletion : object
      EdgeObsoletion : object_type
      EdgeObsoletion : old_datatype
      EdgeObsoletion : old_language
      EdgeObsoletion : old_value
      EdgeObsoletion : old_value_type
      EdgeObsoletion : predicate
      EdgeObsoletion : pull_request
      EdgeObsoletion : see_also
      EdgeObsoletion : subject
      EdgeObsoletion : type
      EdgeObsoletion : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [SimpleChange](SimpleChange.md)
        * [EdgeChange](EdgeChange.md)
            * **EdgeObsoletion** [ obsoletion]



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [subject](subject.md) | 0..1 <br/> [Node](Node.md)  |   |
| [predicate](predicate.md) | 0..1 <br/> [Node](Node.md)  |   |
| [object](object.md) | 0..1 <br/> [Node](Node.md)  |   |
| [annotation_set](annotation_set.md) | 0..1 <br/> [Annotation](Annotation.md)  |   |
| [about_edge](about_edge.md) | 0..1 <br/> [Edge](Edge.md)  |   |
| [object_type](object_type.md) | 0..1 <br/> [xsd:string](xsd:string)  | The type (IRI or Literal) of an object  |
| [language](language.md) | 0..1 <br/> [LanguageTag](LanguageTag.md)  | The language tag of a literal  |
| [datatype](datatype.md) | 0..1 <br/> [xsd:string](xsd:string)  | The datatype of a literal  |
| [old_value](old_value.md) | 0..1 <br/> [xsd:string](xsd:string)  | The value of a property held in the old instance of the ontology  |
| [new_value](new_value.md) | 0..1 <br/> [xsd:string](xsd:string)  | The value of a property held in the new instance of the ontology  |
| [old_value_type](old_value_type.md) | 0..1 <br/> [xsd:string](xsd:string)  | The type (IRI or Literal) of an old value  |
| [new_value_type](new_value_type.md) | 0..1 <br/> [xsd:string](xsd:string)  | The type (IRI or Literal) of a new value  |
| [new_language](new_language.md) | 0..1 <br/> [xsd:string](xsd:string)  | The new language tag of a literal  |
| [old_language](old_language.md) | 0..1 <br/> [xsd:string](xsd:string)  | The old language tag of a literal  |
| [new_datatype](new_datatype.md) | 0..1 <br/> [xsd:string](xsd:string)  | The new datatype of a literal  |
| [old_datatype](old_datatype.md) | 0..1 <br/> [xsd:string](xsd:string)  | The old datatype of a literal  |
| [id](id.md) | 1..1 <br/> [xsd:string](xsd:string)  |   |
| [type](type.md) | 0..1 <br/> [xsd:string](xsd:string)  |   |
| [was_generated_by](was_generated_by.md) | 0..1 <br/> [Activity](Activity.md)  |   |
| [see_also](see_also.md) | 0..1 <br/> [xsd:string](xsd:string)  |   |
| [pull_request](pull_request.md) | 0..1 <br/> [xsd:string](xsd:string)  |   |
| [creator](creator.md) | 0..1 <br/> [xsd:string](xsd:string)  |   |
| [change_date](change_date.md) | 0..1 <br/> [xsd:string](xsd:string)  |   |
| [contributor](contributor.md) | 0..1 <br/> [xsd:string](xsd:string)  |   |
| [has_undo](has_undo.md) | 0..1 <br/> [Obsoletion](Obsoletion.md)  | A change that reverses this change  |


## Usages



## Comments

* Note there is not yet consensus in how this should be done in rdf/owl implementations. Simply marking the edge deprecated with render it visible to most clients. Care must be taken because simply adding a deprecation tag to an axiom does not silence it -- it is still asserted. It is therefore more common to obsolete an edge by shadowing the axiom as an annotation. See the Mondo docs for example

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/hrshdhgd/kgcl-schema







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl_schema:EdgeObsoletion'] |
| native | ['kgcl_schema:EdgeObsoletion'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: edge obsoletion
description: An edge change in which an edge is obsoleted.
comments:
- Note there is not yet consensus in how this should be done in rdf/owl implementations.
  Simply marking the edge deprecated with render it visible to most clients. Care
  must be taken because simply adding a deprecation tag to an axiom does not silence
  it -- it is still asserted. It is therefore more common to obsolete an edge by shadowing
  the axiom as an annotation. See the Mondo docs for example
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
see_also:
- https://mondo.readthedocs.io/en/latest/editors-guide/g-logical-axioms/#excluded-subclassof
aliases:
- relationship obsoletion
rank: 1000
is_a: edge change
mixins:
- obsoletion
slots:
- subject
- predicate
- object
- annotation set
slot_usage:
  change description:
    name: change description
    string_serialization: obsoleting edge {edge}

```
</details>

### Induced

<details>
```yaml
name: edge obsoletion
description: An edge change in which an edge is obsoleted.
comments:
- Note there is not yet consensus in how this should be done in rdf/owl implementations.
  Simply marking the edge deprecated with render it visible to most clients. Care
  must be taken because simply adding a deprecation tag to an axiom does not silence
  it -- it is still asserted. It is therefore more common to obsolete an edge by shadowing
  the axiom as an annotation. See the Mondo docs for example
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
see_also:
- https://mondo.readthedocs.io/en/latest/editors-guide/g-logical-axioms/#excluded-subclassof
aliases:
- relationship obsoletion
rank: 1000
is_a: edge change
mixins:
- obsoletion
slot_usage:
  change description:
    name: change description
    string_serialization: obsoleting edge {edge}
attributes:
  subject:
    name: subject
    from_schema: https://w3id.org/kgcl_schema/ontology
    rank: 1000
    alias: subject
    owner: edge obsoletion
    domain_of:
    - edge creation
    - edge deletion
    - edge obsoletion
    - mapping creation
    - edge
    range: node
  predicate:
    name: predicate
    from_schema: https://w3id.org/kgcl_schema/ontology
    rank: 1000
    alias: predicate
    owner: edge obsoletion
    domain_of:
    - edge creation
    - edge deletion
    - edge obsoletion
    - mapping creation
    - edge
    range: node
  object:
    name: object
    from_schema: https://w3id.org/kgcl_schema/ontology
    rank: 1000
    alias: object
    owner: edge obsoletion
    domain_of:
    - edge creation
    - edge deletion
    - edge obsoletion
    - mapping creation
    - edge
    range: node
  annotation set:
    name: annotation set
    from_schema: https://w3id.org/kgcl_schema/ontology
    rank: 1000
    alias: annotation_set
    owner: edge obsoletion
    domain_of:
    - edge creation
    - edge deletion
    - edge obsoletion
    - mapping creation
    - node creation
    - annotation
    - node
    - edge
    range: annotation
  about edge:
    name: about edge
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    is_a: about
    multivalued: false
    alias: about_edge
    owner: edge obsoletion
    domain_of:
    - edge change
    range: edge
  object type:
    name: object type
    description: The type (IRI or Literal) of an object
    deprecated: no longer required
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: object_type
    owner: edge obsoletion
    domain_of:
    - edge change
    - edge creation
    - edge deletion
    range: string
  language:
    name: language
    description: The language tag of a literal
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: language
    owner: edge obsoletion
    domain_of:
    - edge change
    - node change
    - new synonym
    - node creation
    range: language tag
  datatype:
    name: datatype
    description: The datatype of a literal
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: datatype
    owner: edge obsoletion
    domain_of:
    - edge change
    range: string
  old value:
    name: old value
    description: The value of a property held in the old instance of the ontology
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: old_value
    owner: edge obsoletion
    domain_of:
    - simple change
    - node rename
    - set language for name
    - remove synonym
    - synonym replacement
    - synonym predicate change
    - remove text definition
    - text definition replacement
    range: string
  new value:
    name: new value
    description: The value of a property held in the new instance of the ontology
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: new_value
    owner: edge obsoletion
    domain_of:
    - simple change
    - node rename
    - set language for name
    - new synonym
    - synonym replacement
    - synonym predicate change
    - new text definition
    - text definition replacement
    range: string
  old value type:
    name: old value type
    description: The type (IRI or Literal) of an old value
    deprecated: no longer required
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: old_value_type
    owner: edge obsoletion
    domain_of:
    - simple change
    range: string
  new value type:
    name: new value type
    description: The type (IRI or Literal) of a new value
    deprecated: no longer required
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: new_value_type
    owner: edge obsoletion
    domain_of:
    - simple change
    range: string
  new language:
    name: new language
    description: The new language tag of a literal
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: new_language
    owner: edge obsoletion
    domain_of:
    - simple change
    - node rename
    range: string
  old language:
    name: old language
    description: The old language tag of a literal
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: old_language
    owner: edge obsoletion
    domain_of:
    - simple change
    - node rename
    range: string
  new datatype:
    name: new datatype
    description: The new datatype of a literal
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: new_datatype
    owner: edge obsoletion
    domain_of:
    - simple change
    range: string
  old datatype:
    name: old datatype
    description: The old datatype of a literal
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: old_datatype
    owner: edge obsoletion
    domain_of:
    - simple change
    range: string
  id:
    name: id
    from_schema: https://w3id.org/kgcl_schema/basics
    rank: 1000
    identifier: true
    alias: id
    owner: edge obsoletion
    domain_of:
    - change
    - activity
    - agent
    - node
    range: string
  type:
    name: type
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: rdf:type
    designates_type: true
    alias: type
    owner: edge obsoletion
    domain_of:
    - change
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl_schema/prov
    rank: 1000
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: edge obsoletion
    domain_of:
    - change
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: edge obsoletion
    domain_of:
    - change
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: pull_request
    owner: edge obsoletion
    domain_of:
    - change
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: dcterms:creator
    alias: creator
    owner: edge obsoletion
    domain_of:
    - change
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: dcterms:date
    alias: change_date
    owner: edge obsoletion
    domain_of:
    - change
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: dcterms:creator
    alias: contributor
    owner: edge obsoletion
    domain_of:
    - change
    range: string
  has undo:
    name: has undo
    description: A change that reverses this change
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    domain: change
    multivalued: false
    alias: has_undo
    owner: edge obsoletion
    domain_of:
    - change
    range: obsoletion

```
</details>