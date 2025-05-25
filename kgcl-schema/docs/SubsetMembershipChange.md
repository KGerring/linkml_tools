# Class: SubsetMembershipChange
_A change in the membership status of a node with respect to a subset (view)_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [kgcl_schema:SubsetMembershipChange](https://w3id.org/kgcl-schema/SubsetMembershipChange)




```mermaid
 classDiagram
      ChangeMixin <|-- SubsetMembershipChange
      
      SubsetMembershipChange : in_subset
      

```





## Inheritance
* [ChangeMixin](ChangeMixin.md)
    * **SubsetMembershipChange**
        * [AddToSubset](AddToSubset.md)
        * [RemoveFromSubset](RemoveFromSubset.md)



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [in_subset](in_subset.md) | 0..1 <br/> [OntologySubset](OntologySubset.md)  | The subset that pertains to this change  |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/hrshdhgd/kgcl-schema







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['kgcl_schema:SubsetMembershipChange'] |
| native | ['kgcl_schema:SubsetMembershipChange'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: subset membership change
description: A change in the membership status of a node with respect to a subset
  (view)
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
rank: 1000
is_a: change mixin
mixin: true
slots:
- in subset

```
</details>

### Induced

<details>
```yaml
name: subset membership change
description: A change in the membership status of a node with respect to a subset
  (view)
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
rank: 1000
is_a: change mixin
mixin: true
attributes:
  in subset:
    name: in subset
    description: The subset that pertains to this change
    from_schema: https://w3id.org/hrshdhgd/kgcl-schema
    rank: 1000
    alias: in_subset
    owner: subset membership change
    domain_of:
    - subset membership change
    range: ontology subset

```
</details>