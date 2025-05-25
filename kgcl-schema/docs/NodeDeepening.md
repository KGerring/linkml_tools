# Class: NodeDeepening
_A node move in which a node where the destination is a proper descendant of the original location. Note that here descendant applied not just to subclass, but edges of any predicate in the relational graph_





URI: [kgcl_schema:NodeDeepening](https://w3id.org/kgcl-schema/NodeDeepening)




```mermaid
 classDiagram
      NodeMove <|-- NodeDeepening
      
      NodeDeepening : about_edge
      NodeDeepening : change_date
      NodeDeepening : contributor
      NodeDeepening : creator
      NodeDeepening : datatype
      NodeDeepening : has_undo
      NodeDeepening : id
      NodeDeepening : language
      NodeDeepening : new_datatype
      NodeDeepening : new_language
      NodeDeepening : new_object_type
      NodeDeepening : new_value
      NodeDeepening : new_value_type
      NodeDeepening : object_type
      NodeDeepening : old_datatype
      NodeDeepening : old_language
      NodeDeepening : old_object_type
      NodeDeepening : old_value
      NodeDeepening : old_value_type
      NodeDeepening : pull_request
      NodeDeepening : see_also
      NodeDeepening : type
      NodeDeepening : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [SimpleChange](SimpleChange.md)
        * [EdgeChange](EdgeChange.md)
            * [NodeMove](NodeMove.md)
                * **NodeDeepening**



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [old_object_type](old_object_type.md) | 0..1 <br/> [xsd:string](xsd:string)  | The type (IRI or Literal) of an old object  |
| [new_object_type](new_object_type.md) | 0..1 <br/> [xsd:string](xsd:string)  | The type (IRI or Literal) of a new object  |
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



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/hrshdhgd/kgcl-schema







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl_schema:NodeDeepening'] |
| native | ['kgcl_schema:NodeDeepening'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: node deepening
description: A node move in which a node where the destination is a proper descendant
  of the original location. Note that here descendant applied not just to subclass,
  but edges of any predicate in the relational graph
examples:
- value: changing a is-a b to a is-a c, where c is a subclass of b
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
rank: 1000
is_a: node move
slot_usage:
  change description:
    name: change description
    string_serialization: deepened {about edge} from {old value} to {new value}

```
</details>

### Induced

<details>
```yaml
name: node deepening
description: A node move in which a node where the destination is a proper descendant
  of the original location. Note that here descendant applied not just to subclass,
  but edges of any predicate in the relational graph
examples:
- value: changing a is-a b to a is-a c, where c is a subclass of b
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
rank: 1000
is_a: node move
slot_usage:
  change description:
    name: change description
    string_serialization: deepened {about edge} from {old value} to {new value}
attributes:
  old object type:
    name: old object type
    description: The type (IRI or Literal) of an old object
    deprecated: no longer required
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: old_object_type
    owner: node deepening
    domain_of:
    - node move
    range: string
  new object type:
    name: new object type
    description: The type (IRI or Literal) of a new object
    deprecated: no longer required
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: new_object_type
    owner: node deepening
    domain_of:
    - node move
    range: string
  about edge:
    name: about edge
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    is_a: about
    multivalued: false
    alias: about_edge
    owner: node deepening
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
    owner: node deepening
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
    owner: node deepening
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
    owner: node deepening
    domain_of:
    - edge change
    range: string
  old value:
    name: old value
    description: The value of a property held in the old instance of the ontology
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: old_value
    owner: node deepening
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
    owner: node deepening
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
    owner: node deepening
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
    owner: node deepening
    domain_of:
    - simple change
    range: string
  new language:
    name: new language
    description: The new language tag of a literal
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: new_language
    owner: node deepening
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
    owner: node deepening
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
    owner: node deepening
    domain_of:
    - simple change
    range: string
  old datatype:
    name: old datatype
    description: The old datatype of a literal
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: old_datatype
    owner: node deepening
    domain_of:
    - simple change
    range: string
  id:
    name: id
    from_schema: https://w3id.org/kgcl_schema/basics
    rank: 1000
    identifier: true
    alias: id
    owner: node deepening
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
    owner: node deepening
    domain_of:
    - change
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl_schema/prov
    rank: 1000
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: node deepening
    domain_of:
    - change
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: node deepening
    domain_of:
    - change
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: pull_request
    owner: node deepening
    domain_of:
    - change
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: dcterms:creator
    alias: creator
    owner: node deepening
    domain_of:
    - change
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: dcterms:date
    alias: change_date
    owner: node deepening
    domain_of:
    - change
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: dcterms:creator
    alias: contributor
    owner: node deepening
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
    owner: node deepening
    domain_of:
    - change
    range: change

```
</details>