# Class: OntologyElement
_Any component of an ontology or knowledge graph_





URI: [om:OntologyElement](om:OntologyElement)




```mermaid
 classDiagram
      OntologyElement <|-- PropertyValue
      OntologyElement <|-- Node
      OntologyElement <|-- Edge
      OntologyElement <|-- LogicalDefinition
      OntologyElement <|-- OntologySubset
      
      
```





## Inheritance
* **OntologyElement**
    * [PropertyValue](PropertyValue.md)
    * [Node](Node.md)
    * [Edge](Edge.md)
    * [LogicalDefinition](LogicalDefinition.md)
    * [OntologySubset](OntologySubset.md)



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl_schema/ontology







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['om:OntologyElement'] |
| native | ['om:OntologyElement'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ontology element
description: Any component of an ontology or knowledge graph
from_schema: https://w3id.org/kgcl_schema/ontology
aliases:
- entity
rank: 1000

```
</details>

### Induced

<details>
```yaml
name: ontology element
description: Any component of an ontology or knowledge graph
from_schema: https://w3id.org/kgcl_schema/ontology
aliases:
- entity
rank: 1000

```
</details>