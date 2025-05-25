# Class: EdgeChange
_A change in which the element that is the focus of the change is an edge._



* __NOTE__: this is an abstract class and should not be instantiated directly



URI: [kgcl_schema:EdgeChange](https://w3id.org/kgcl-schema/EdgeChange)




```mermaid
 classDiagram
      SimpleChange <|-- EdgeChange
      
      EdgeChange : about_edge
      EdgeChange : change_date
      EdgeChange : contributor
      EdgeChange : creator
      EdgeChange : datatype
      EdgeChange : has_undo
      EdgeChange : id
      EdgeChange : language
      EdgeChange : new_datatype
      EdgeChange : new_language
      EdgeChange : new_value
      EdgeChange : new_value_type
      EdgeChange : object_type
      EdgeChange : old_datatype
      EdgeChange : old_language
      EdgeChange : old_value
      EdgeChange : old_value_type
      EdgeChange : pull_request
      EdgeChange : see_also
      EdgeChange : type
      EdgeChange : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [SimpleChange](SimpleChange.md)
        * **EdgeChange**
            * [EdgeCreation](EdgeCreation.md) [ creation]
            * [EdgeDeletion](EdgeDeletion.md) [ deletion]
            * [EdgeObsoletion](EdgeObsoletion.md) [ obsoletion]
            * [EdgeRewiring](EdgeRewiring.md)
            * [NodeMove](NodeMove.md)
            * [PredicateChange](PredicateChange.md)
            * [EdgeLogicalInterpretationChange](EdgeLogicalInterpretationChange.md)



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
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
| [has_undo](has_undo.md) | 0..1 <br/> [Change](Change.md)  | A change that reverses this change  |


## Usages



## TODOs

* decide on flat serialization, see https://github.com/cmungall/knowledge-graph-change-language/issues/7

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/hrshdhgd/kgcl-schema







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl_schema:EdgeChange'] |
| native | ['kgcl_schema:EdgeChange'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: edge change
description: A change in which the element that is the focus of the change is an edge.
todos:
- decide on flat serialization, see https://github.com/cmungall/knowledge-graph-change-language/issues/7
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
aliases:
- axiom change
- triple change
rank: 1000
is_a: simple change
abstract: true
slots:
- about edge
- object type
- language
- datatype
slot_usage:
  subject:
    name: subject
    comments:
    - if subject is empty, use the about field of the last node change

```
</details>

### Induced

<details>
```yaml
name: edge change
description: A change in which the element that is the focus of the change is an edge.
todos:
- decide on flat serialization, see https://github.com/cmungall/knowledge-graph-change-language/issues/7
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
aliases:
- axiom change
- triple change
rank: 1000
is_a: simple change
abstract: true
slot_usage:
  subject:
    name: subject
    comments:
    - if subject is empty, use the about field of the last node change
attributes:
  about edge:
    name: about edge
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    is_a: about
    multivalued: false
    alias: about_edge
    owner: edge change
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
    owner: edge change
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
    owner: edge change
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
    owner: edge change
    domain_of:
    - edge change
    range: string
  old value:
    name: old value
    description: The value of a property held in the old instance of the ontology
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: old_value
    owner: edge change
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
    owner: edge change
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
    owner: edge change
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
    owner: edge change
    domain_of:
    - simple change
    range: string
  new language:
    name: new language
    description: The new language tag of a literal
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: new_language
    owner: edge change
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
    owner: edge change
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
    owner: edge change
    domain_of:
    - simple change
    range: string
  old datatype:
    name: old datatype
    description: The old datatype of a literal
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: old_datatype
    owner: edge change
    domain_of:
    - simple change
    range: string
  id:
    name: id
    from_schema: https://w3id.org/kgcl_schema/basics
    rank: 1000
    identifier: true
    alias: id
    owner: edge change
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
    owner: edge change
    domain_of:
    - change
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl_schema/prov
    rank: 1000
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: edge change
    domain_of:
    - change
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: edge change
    domain_of:
    - change
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: pull_request
    owner: edge change
    domain_of:
    - change
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: dcterms:creator
    alias: creator
    owner: edge change
    domain_of:
    - change
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: dcterms:date
    alias: change_date
    owner: edge change
    domain_of:
    - change
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: dcterms:creator
    alias: contributor
    owner: edge change
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
    owner: edge change
    domain_of:
    - change
    range: change

```
</details>