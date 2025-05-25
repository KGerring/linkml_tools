# Class: Annotation
_owl annotations. Not to be confused with annotations sensu GO_





URI: [om:Annotation](om:Annotation)




```mermaid
 classDiagram
      PropertyValue <|-- Annotation
      
      Annotation : annotation_set
      Annotation : filler
      Annotation : filler_type
      Annotation : property
      Annotation : property_type
      

```





## Inheritance
* [OntologyElement](OntologyElement.md)
    * [PropertyValue](PropertyValue.md)
        * **Annotation**



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [property](property.md) | 0..1 <br/> [Node](Node.md)  |   |
| [filler](filler.md) | 0..1 <br/> [xsd:string](xsd:string)  |   |
| [annotation_set](annotation_set.md) | 0..1 <br/> [Annotation](Annotation.md)  |   |
| [property_type](property_type.md) | 0..1 <br/> [xsd:string](xsd:string)  |   |
| [filler_type](filler_type.md) | 0..1 <br/> [xsd:string](xsd:string)  |   |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EdgeCreation](EdgeCreation.md) | [annotation_set](annotation_set.md) | range | annotation |
| [PlaceUnder](PlaceUnder.md) | [annotation_set](annotation_set.md) | range | annotation |
| [EdgeDeletion](EdgeDeletion.md) | [annotation_set](annotation_set.md) | range | annotation |
| [RemoveUnder](RemoveUnder.md) | [annotation_set](annotation_set.md) | range | annotation |
| [EdgeObsoletion](EdgeObsoletion.md) | [annotation_set](annotation_set.md) | range | annotation |
| [MappingCreation](MappingCreation.md) | [annotation_set](annotation_set.md) | range | annotation |
| [NodeCreation](NodeCreation.md) | [annotation_set](annotation_set.md) | range | annotation |
| [ClassCreation](ClassCreation.md) | [annotation_set](annotation_set.md) | range | annotation |
| [Annotation](Annotation.md) | [annotation_set](annotation_set.md) | range | annotation |
| [Node](Node.md) | [annotation_set](annotation_set.md) | range | annotation |
| [ClassNode](ClassNode.md) | [annotation_set](annotation_set.md) | range | annotation |
| [InstanceNode](InstanceNode.md) | [annotation_set](annotation_set.md) | range | annotation |
| [Edge](Edge.md) | [annotation_set](annotation_set.md) | range | annotation |



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/kgcl_schema/ontology







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['om:Annotation'] |
| native | ['om:Annotation'] |
| undefined | ['owl:Annotation'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: annotation
description: owl annotations. Not to be confused with annotations sensu GO
from_schema: https://w3id.org/kgcl_schema/ontology
mappings:
- owl:Annotation
rank: 1000
is_a: property value
slots:
- property
- filler
- annotation set
- property type
- filler type

```
</details>

### Induced

<details>
```yaml
name: annotation
description: owl annotations. Not to be confused with annotations sensu GO
from_schema: https://w3id.org/kgcl_schema/ontology
mappings:
- owl:Annotation
rank: 1000
is_a: property value
attributes:
  property:
    name: property
    from_schema: https://w3id.org/kgcl_schema/ontology
    rank: 1000
    alias: property
    owner: annotation
    domain_of:
    - property value
    - annotation
    range: node
  filler:
    name: filler
    from_schema: https://w3id.org/kgcl_schema/ontology
    rank: 1000
    alias: filler
    owner: annotation
    domain_of:
    - property value
    - annotation
    range: string
  annotation set:
    name: annotation set
    from_schema: https://w3id.org/kgcl_schema/ontology
    rank: 1000
    alias: annotation_set
    owner: annotation
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
  property type:
    name: property type
    deprecated: no longer required
    from_schema: https://w3id.org/kgcl_schema/ontology
    rank: 1000
    alias: property_type
    owner: annotation
    domain_of:
    - annotation
    range: string
  filler type:
    name: filler type
    deprecated: no longer required
    from_schema: https://w3id.org/kgcl_schema/ontology
    rank: 1000
    alias: filler_type
    owner: annotation
    domain_of:
    - annotation
    range: string

```
</details>