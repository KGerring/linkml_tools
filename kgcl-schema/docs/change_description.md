# Slot: change_description
_A string serialization of the change. This should be both human-readable, and parseable._


URI: [https://w3id.org/kgcl-schema/change_description](https://w3id.org/kgcl-schema/change_description)



<!-- no inheritance hierarchy -->




## Properties

* Range: [xsd:string](xsd:string)
* Multivalued: None







## Comments

* {'Form 1': 'IRIs are denoted by CURIEs, optionally followed by label in parenthesis'}
* {'Form 2': "IRIs are denoted by the rdfs:label in single quotes, e.g. 'nervous system'"}

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/hrshdhgd/kgcl-schema




## LinkML Specification

<details>
```yaml
name: change description
description: A string serialization of the change. This should be both human-readable,
  and parseable.
comments:
- '{''Form 1'': ''IRIs are denoted by CURIEs, optionally followed by label in parenthesis''}'
- '{''Form 2'': "IRIs are denoted by the rdfs:label in single quotes, e.g. ''nervous
  system''"}'
examples:
- value: rename UBERON:0002398 from 'manus' to 'hand'
- value: move 'hand' from 'part of' 'hindlimb' to 'part of' 'forelimb'
- value: merge 'cellular metabolic process' into 'metabolic process'
- value: search and replace 'metabolic process' with 'metabolism' in all labels under
    'biological process'
- value: search and replace 'metabolic process' with 'metabolism' in all labels under
    'biological process' retaining as 'exact synonym'
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
rank: 1000
alias: change_description
range: string

```
</details>