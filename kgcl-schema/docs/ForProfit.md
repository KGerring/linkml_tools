# Class: ForProfit




URI: [TEMP:ForProfit](https://example.org/TEMP/ForProfit)




```mermaid
 classDiagram
      Organization <|-- ForProfit
      
      ForProfit : name
      

```





## Inheritance
* [Organization](Organization.md)
    * **ForProfit**



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [name](name.md) | 1..1 <br/> [xsd:string](xsd:string)  |   |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: TEMP







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['TEMP:ForProfit'] |
| native | ['TEMP:ForProfit'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ForProfit
from_schema: TEMP
rank: 1000
is_a: Organization

```
</details>

### Induced

<details>
```yaml
name: ForProfit
from_schema: TEMP
rank: 1000
is_a: Organization
attributes:
  name:
    name: name
    from_schema: TEMP
    rank: 1000
    multivalued: false
    alias: name
    owner: ForProfit
    domain_of:
    - Person
    - Organization
    range: string
    required: true

```
</details>