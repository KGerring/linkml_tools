# Class: MultiNodeObsoletion
_A complex change consisting of multiple obsoletions._





URI: [kgcl_schema:MultiNodeObsoletion](https://w3id.org/kgcl-schema/MultiNodeObsoletion)




```mermaid
 classDiagram
      ComplexChange <|-- MultiNodeObsoletion
      
      MultiNodeObsoletion : change_date
      MultiNodeObsoletion : change_set
      MultiNodeObsoletion : contributor
      MultiNodeObsoletion : creator
      MultiNodeObsoletion : has_undo
      MultiNodeObsoletion : id
      MultiNodeObsoletion : pull_request
      MultiNodeObsoletion : see_also
      MultiNodeObsoletion : type
      MultiNodeObsoletion : was_generated_by
      

```





## Inheritance
* [Change](Change.md)
    * [ComplexChange](ComplexChange.md)
        * **MultiNodeObsoletion**



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [change_set](change_set.md) | 0..* <br/> [NodeObsoletion](NodeObsoletion.md)  | A collection of changes  |
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
| self | ['kgcl_schema:MultiNodeObsoletion'] |
| native | ['kgcl_schema:MultiNodeObsoletion'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: multi node obsoletion
description: A complex change consisting of multiple obsoletions.
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
see_also:
- https://github.com/cmungall/obo-scripts/blob/master/obo-obsoletify.pl
aliases:
- multi node deprecation
- multi class obsoletion
- multi term obsoletion
- multi concept obsoletion
rank: 1000
is_a: complex change
slot_usage:
  change set:
    name: change set
    domain_of:
    - complex change
    - transaction
    - session
    - complex change
    - transaction
    - session
    range: node obsoletion
  change description:
    name: change description
    string_serialization: a multi node obsoletion consisting of {change set}
  associated change set:
    name: associated change set
    description: "All changes associated with a set of obsoletions. This change set\
      \ is the composed change set rather than the set of individual changes. For\
      \ example, if previous state is:\n  `A subClassOf B subClassOf C subClassOf\
      \ D`\nand we obsolete {B,C}, then the individual changes are `A moves from B\
      \ to C` and `B moves from C to D`, but the composed change set is `A moves from\
      \ B to D`"
    is_a: change set

```
</details>

### Induced

<details>
```yaml
name: multi node obsoletion
description: A complex change consisting of multiple obsoletions.
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
see_also:
- https://github.com/cmungall/obo-scripts/blob/master/obo-obsoletify.pl
aliases:
- multi node deprecation
- multi class obsoletion
- multi term obsoletion
- multi concept obsoletion
rank: 1000
is_a: complex change
slot_usage:
  change set:
    name: change set
    domain_of:
    - complex change
    - transaction
    - session
    - complex change
    - transaction
    - session
    range: node obsoletion
  change description:
    name: change description
    string_serialization: a multi node obsoletion consisting of {change set}
  associated change set:
    name: associated change set
    description: "All changes associated with a set of obsoletions. This change set\
      \ is the composed change set rather than the set of individual changes. For\
      \ example, if previous state is:\n  `A subClassOf B subClassOf C subClassOf\
      \ D`\nand we obsolete {B,C}, then the individual changes are `A moves from B\
      \ to C` and `B moves from C to D`, but the composed change set is `A moves from\
      \ B to D`"
    is_a: change set
attributes:
  change set:
    name: change set
    description: A collection of changes
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    multivalued: true
    alias: change_set
    owner: multi node obsoletion
    domain_of:
    - complex change
    - transaction
    - session
    - complex change
    - transaction
    - session
    range: node obsoletion
    inlined: true
    inlined_as_list: true
  id:
    name: id
    from_schema: https://w3id.org/kgcl_schema/basics
    rank: 1000
    identifier: true
    alias: id
    owner: multi node obsoletion
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
    owner: multi node obsoletion
    domain_of:
    - change
    range: string
  was generated by:
    name: was generated by
    from_schema: https://w3id.org/kgcl_schema/prov
    rank: 1000
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: multi node obsoletion
    domain_of:
    - change
    range: activity
  see also:
    name: see also
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: rdfs:seeAlso
    alias: see_also
    owner: multi node obsoletion
    domain_of:
    - change
    range: string
  pull request:
    name: pull request
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: pull_request
    owner: multi node obsoletion
    domain_of:
    - change
    range: string
  creator:
    name: creator
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: dcterms:creator
    alias: creator
    owner: multi node obsoletion
    domain_of:
    - change
    range: string
  change date:
    name: change date
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: dcterms:date
    alias: change_date
    owner: multi node obsoletion
    domain_of:
    - change
    range: string
  contributor:
    name: contributor
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    slot_uri: dcterms:creator
    alias: contributor
    owner: multi node obsoletion
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
    owner: multi node obsoletion
    domain_of:
    - change
    range: change

```
</details>