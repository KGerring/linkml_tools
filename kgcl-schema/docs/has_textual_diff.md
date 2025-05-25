# Slot: has_textual_diff
_A representation of character-level changes on a textual literal property. For example, if a text definition may change by only a single character such as addition of a period, it is useful to be able to see this visually._


URI: [https://w3id.org/kgcl-schema/has_textual_diff](https://w3id.org/kgcl-schema/has_textual_diff)



<!-- no inheritance hierarchy -->




## Properties

* Range: [TextualDiff](TextualDiff.md)
* Multivalued: None







## Comments

* this is NOT for representing the diff of the change as a whole.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/hrshdhgd/kgcl-schema




## LinkML Specification

<details>
```yaml
name: has textual diff
description: A representation of character-level changes on a textual literal property.
  For example, if a text definition may change by only a single character such as
  addition of a period, it is useful to be able to see this visually.
comments:
- this is NOT for representing the diff of the change as a whole.
from_schema: https://w3id.org/hrshdhgd/kgcl-schema
rank: 1000
domain: change
alias: has_textual_diff
domain_of:
- node rename
- synonym replacement
- synonym predicate change
- text definition replacement
range: textual diff

```
</details>