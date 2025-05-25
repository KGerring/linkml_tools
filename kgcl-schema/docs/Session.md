# Class: Session
_A session consists of a set of change sets bundled with the activities that generated those change sets_





URI: [kgcl_schema:Session](https://w3id.org/kgcl-schema/Session)




```mermaid
 classDiagram
    class Session
      Session : activity_set
      Session : change_set
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [change_set](change_set.md) | 0..* <br/> [Change](Change.md)  | A collection of changes  |
| [activity_set](activity_set.md) | 0..* <br/> [Activity](Activity.md)  |   |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/hrshdhgd/kgcl-schema







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl_schema:Session'] |
| native | ['kgcl_schema:Session'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: session
description: A session consists of a set of change sets bundled with the activities
  that generated those change sets
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
rank: 1000
slots:
- change set
- activity set

```
</details>

### Induced

<details>
```yaml
name: session
description: A session consists of a set of change sets bundled with the activities
  that generated those change sets
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
rank: 1000
attributes:
  change set:
    name: change set
    description: A collection of changes
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    multivalued: true
    alias: change_set
    owner: session
    domain_of:
    - complex change
    - transaction
    - session
    range: change
    inlined: true
    inlined_as_list: true
  activity set:
    name: activity set
    from_schema: https://w3id.org/kgcl_schema/prov
    rank: 1000
    multivalued: true
    alias: activity_set
    owner: session
    domain_of:
    - session
    range: activity
    inlined: true
    inlined_as_list: true

```
</details>