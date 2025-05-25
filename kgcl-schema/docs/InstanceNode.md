# Class: InstanceNode
_A node that is an individual_





URI: [owl:NamedIndividual](owl:NamedIndividual)




```mermaid
 classDiagram
      Node <|-- InstanceNode
      
      InstanceNode : annotation_set
      InstanceNode : id
      InstanceNode : name
      InstanceNode : owl_type
      

```





## Inheritance
* [OntologyElement](OntologyElement.md)
    * [Node](Node.md)
        * **InstanceNode**



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [id](id.md) | 1..1 <br/> [xsd:string](xsd:string)  |   |
| [name](name.md) | 0..1 <br/> [xsd:string](xsd:string)  |   |
| [annotation_set](annotation_set.md) | 0..1 <br/> [Annotation](Annotation.md)  |   |
| [owl_type](owl_type.md) | 0..1 <br/> [OwlTypeEnum](OwlTypeEnum.md)  |   |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl_schema/ontology







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['owl:NamedIndividual'] |
| native | ['om:InstanceNode'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: instance node
description: A node that is an individual
from_schema: https://w3id.org/kgcl_schema/ontology
aliases:
- named individual
rank: 1000
is_a: node
class_uri: owl:NamedIndividual

```
</details>

### Induced

<details>
```yaml
name: instance node
description: A node that is an individual
from_schema: https://w3id.org/kgcl_schema/ontology
aliases:
- named individual
rank: 1000
is_a: node
attributes:
  id:
    name: id
    from_schema: https://w3id.org/kgcl_schema/basics
    rank: 1000
    identifier: true
    alias: id
    owner: instance node
    domain_of:
    - change
    - activity
    - agent
    - node
    range: string
  name:
    name: name
    from_schema: https://w3id.org/kgcl_schema/ontology
    rank: 1000
    alias: name
    owner: instance node
    domain_of:
    - node creation
    - node
    range: string
  annotation set:
    name: annotation set
    from_schema: https://w3id.org/kgcl_schema/ontology
    rank: 1000
    alias: annotation_set
    owner: instance node
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
  owl type:
    name: owl type
    from_schema: https://w3id.org/kgcl_schema/ontology
    rank: 1000
    alias: owl_type
    owner: instance node
    domain_of:
    - node creation
    - node
    range: owl_type_enum
class_uri: owl:NamedIndividual

```
</details>