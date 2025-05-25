# Slot: has_nondirect_replacement
_An obsoletion replacement where it is NOT valid to automatically update annotations/edges pointing at the node with its direct replacement_


URI: [https://w3id.org/kgcl-schema/has_nondirect_replacement](https://w3id.org/kgcl-schema/has_nondirect_replacement)



<!-- no inheritance hierarchy -->




## Properties

* Range: [Node](Node.md)
* Multivalued: True







## Comments

* if a node obsoletion C, C about N1, and C has direct replacement N2, and there exists an edge with an edge property referencing N1, it is possible to replace with N2
* if a node obsoletion C C about N1, and Chas direct replacement N2, then N1 oio:consider N2

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/hrshdhgd/kgcl-schema




## LinkML Specification

<details>
```yaml
name: has nondirect replacement
description: An obsoletion replacement where it is NOT valid to automatically update
  annotations/edges pointing at the node with its direct replacement
comments:
- if a node obsoletion C, C about N1, and C has direct replacement N2, and there exists
  an edge with an edge property referencing N1, it is possible to replace with N2
- if a node obsoletion C C about N1, and Chas direct replacement N2, then N1 oio:consider
  N2
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
close_mappings:
- oio:consider
rank: 1000
multivalued: true
alias: has_nondirect_replacement
domain_of:
- node obsoletion
range: node

```
</details>