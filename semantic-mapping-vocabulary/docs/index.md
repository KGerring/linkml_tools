# Semantic Mapping Vocabulary

## Metadata

**IRI**

`http://w3id.org/semapv/vocab/semapv.owl`

[Title](http://purl.org/dc/terms/title "A name given to the resource. Defined in DCMI Metadata Terms")

Semantic Mapping Vocabulary

[License](http://purl.org/dc/terms/license "A legal document giving official permission to do something with the resource. Defined in DCMI Metadata Terms")

[https://creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/)

[Version Iri](http://www.w3.org/2002/07/owl#versionIRI "The property that identifies the version IRI of an ontology. Defined in The OWL 2 Schema vocabulary (OWL 2)")

[http://w3id.org/semapv/vocab/releases/2025-01-06/semapv.owl](http://w3id.org/semapv/vocab/releases/2025-01-06/semapv.owl)

[Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

The Semantic Mapping Vocabulary provides and defines terms used for creating and maintaining semantic mappings, in particular mapping metadata.

## Classes

### background knowledge-based matching process c

IRI `https://w3id.org/semapv/vocab/BackgroundKnowledgeBasedMatching` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A matching process that exploits background knowledge from external resources, commonly referred to as background knowledge resources. This approach is also known as indirect matching, BK-based matching or context-based matching.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
A match between a subject A and an object B was established because they appear equivalent under consideration of externally provided background knowledge.
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1016/j.websem.2018.04.001](https://doi.org/10.1016/j.websem.2018.04.001) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process](https://w3id.org/semapv/vocab/Matching) c

### blank normalisation c

IRI `https://w3id.org/semapv/vocab/BlankNormalisation` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A normalization technique replacing all blank characters, such as space, tabulation, carriage return (or sequences of these) into a single blank character.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
The string 'ontology  matching' (two spaces between 'ontology' and 'matching) becomes 'ontology matching' (one space).
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### cardinality filtering c

IRI `https://w3id.org/semapv/vocab/CardinalityFiltering` [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process post-processing](https://w3id.org/semapv/vocab/MatchingPostProcessing) c

### case normalization c

IRI `https://w3id.org/semapv/vocab/CaseNormalization` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A normalization technique converting each alphabetic character in a string to their lower case counterpart.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
The string 'Ontology' is normalised to 'ontology' (lower case).
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### composite matching process c

IRI `https://w3id.org/semapv/vocab/CompositeMatching` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A matching process based on multiple, possibly intertwined, matching approaches.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
An ontology matching tool determines that a subject should be mapped to an object by employing a range of techniques, including lexical, semantic and structural.
```

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process](https://w3id.org/semapv/vocab/Matching) c

### diacritics suppression c

IRI `https://w3id.org/semapv/vocab/DiacriticsSuppression` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A normalization technique replacing diactritic signs (e.g. accents, hats) with their most frequent replacements.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
The string 'Protégé' is normalised to 'Protege'.
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### digit suppression c

IRI `https://w3id.org/semapv/vocab/DigitSuppression` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A normalization technique removing all numbers in a string.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
The string 'ontology1' becomes 'ontology'.
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### edit distance c

IRI `https://w3id.org/semapv/vocab/EditDistance` [Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [string-based similarity measure](https://w3id.org/semapv/vocab/StringBasedSimilarityMeasure) c [Super Class Of](https://w3id.org/profile/ontdoc/superClassOf "Inverse of RDFS' subClassOf. Defined in Ontology Documentation Profile") [levenshtein distance](https://w3id.org/semapv/vocab/LevenshteinEditDistance) c

### hamming distance c

IRI `https://w3id.org/semapv/vocab/HammingDistance` [Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [string-based similarity measure](https://w3id.org/semapv/vocab/StringBasedSimilarityMeasure) c

### instance-based matching process c

IRI `https://w3id.org/semapv/vocab/InstanceBasedMatching` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A matching process based on individual representations (or instances).

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
A match between a subject A and an object B was established because they share the same instances.
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process](https://w3id.org/semapv/vocab/Matching) c

### language-based similarity measure c

IRI `https://w3id.org/semapv/vocab/LanguageBasedSimilarityMeasure` [Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [similarity measure](https://w3id.org/semapv/vocab/SimilarityMeasure) c

### lemmatization c

IRI `https://w3id.org/semapv/vocab/Lemmatization` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

The process of reducing the different forms of a word to one single form.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### levenshtein distance c

IRI `https://w3id.org/semapv/vocab/LevenshteinEditDistance` [Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [edit distance](https://w3id.org/semapv/vocab/EditDistance) c

### lexical matching process c

IRI `https://w3id.org/semapv/vocab/LexicalMatching` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A matching process based on a lexical comparison between one or more syntactic features of the subject with one or more syntactic features of the object.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
The label of a subject entity matches to an exact synonym of an object entity.
```

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process](https://w3id.org/semapv/vocab/Matching) c

### lexical similarity threshold-based matching process c

IRI `https://w3id.org/semapv/vocab/LexicalSimilarityThresholdMatching` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A lexical matching process based on a minimum threshold of a score from a comparison based on a lexical similarity algorithm.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
A match between a subject and an object was established because they had a Levenshtein score higher than 0.8.
```

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process](https://w3id.org/semapv/vocab/Matching) c

### link stripping c

IRI `https://w3id.org/semapv/vocab/LinkStripping` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A normalization technique replacing specific links between words, such as apostrophes, dashes, underscore, etc into dashes or blanks.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
The string 'alzheimer's' becomes 'alzheimers'.
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### logical consistency filtering c

IRI `https://w3id.org/semapv/vocab/LogicalConsistencyFiltering` [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process post-processing](https://w3id.org/semapv/vocab/MatchingPostProcessing) c

### logical reasoning matching process c

IRI `https://w3id.org/semapv/vocab/LogicalReasoning` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A matching process based on the inferences made by a logical reasoner.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
Two classes across ontologies are determined equivalent by an OWL reasoner such as ELK.
```

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process](https://w3id.org/semapv/vocab/Matching) c

### manual mapping curation c

IRI `https://w3id.org/semapv/vocab/ManualMappingCuration` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

An matching process that is performed by a human agent and is based on human judgement and domain knowledge.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
A human curator determines that a subject should be mapped to an object by virtue of their domain expertise.
```

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process](https://w3id.org/semapv/vocab/Matching) c

### mapping c

IRI `https://w3id.org/semapv/vocab/Mapping` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A triple comprising a subject entity s, an object entity o and a mapping predicate p.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
The subject entity NCI:C9305 is mapped to the object entity ICD10:C80.9 using the skos:relatedMatch mapping predicate.
```

### mapping activity c

IRI `https://w3id.org/semapv/vocab/MappingActivity` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A process that relates to the creation, confirmation, rejection or curation of a mapping.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
Matching is a mapping activity that results in the creating of a mapping; mapping review is an activity that results in the confirmation of a mapping.
```

[Super Class Of](https://w3id.org/profile/ontdoc/superClassOf "Inverse of RDFS' subClassOf. Defined in Ontology Documentation Profile")

- [mapping review](https://w3id.org/semapv/vocab/MappingReview) c
- [matching process](https://w3id.org/semapv/vocab/Matching) c
- [matching process post-processing](https://w3id.org/semapv/vocab/MatchingPostProcessing) c
- [matching process pre-processing](https://w3id.org/semapv/vocab/MatchingPreprocessing) c

### mapping chaining-based matching process c

IRI `https://w3id.org/semapv/vocab/MappingChaining` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A matching process based on the traversing of multiple mappings.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
A match between a subject A and an object B was established because A was mapped to C, C was mapped to D and D was mapped to B.
```

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process](https://w3id.org/semapv/vocab/Matching) c

### mapping inversion-based matching process c

IRI `https://w3id.org/semapv/vocab/MappingInversion` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A matching process based on the inverting or flipping of the subject with the object of a mapping in accordance with the semantics of the mapping predicate.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
A broad match between a subject A and an object B using the skos:narrowMatch mapping relation was established because B was mapped to A using the skos:broadMatch mapping relation.
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://mapping-commons.github.io/sssom/chaining\_rules/](https://mapping-commons.github.io/sssom/chaining_rules/) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process](https://w3id.org/semapv/vocab/Matching) c

### mapping review c

IRI `https://w3id.org/semapv/vocab/MappingReview` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A process that is concerned with determining if a mapping “candidate” (otherwise determined) is reasonable/correct.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
A match between a subject A and an object B was established elsewhere, and a human reviewer determined that the mapping is true (or false) based on an independent evaluation.
```

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [mapping activity](https://w3id.org/semapv/vocab/MappingActivity) c

### matching process c

IRI `https://w3id.org/semapv/vocab/Matching` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

An process that results in a mapping between a subject and an object entity.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
The label of a subject entity matches to an exact synonym of an object entity.
```

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [mapping activity](https://w3id.org/semapv/vocab/MappingActivity) c [Super Class Of](https://w3id.org/profile/ontdoc/superClassOf "Inverse of RDFS' subClassOf. Defined in Ontology Documentation Profile")

- [background knowledge-based matching process](https://w3id.org/semapv/vocab/BackgroundKnowledgeBasedMatching) c
- [composite matching process](https://w3id.org/semapv/vocab/CompositeMatching) c
- [instance-based matching process](https://w3id.org/semapv/vocab/InstanceBasedMatching) c
- [lexical matching process](https://w3id.org/semapv/vocab/LexicalMatching) c
- [lexical similarity threshold-based matching process](https://w3id.org/semapv/vocab/LexicalSimilarityThresholdMatching) c
- [logical reasoning matching process](https://w3id.org/semapv/vocab/LogicalReasoning) c
- [manual mapping curation](https://w3id.org/semapv/vocab/ManualMappingCuration) c
- [mapping chaining-based matching process](https://w3id.org/semapv/vocab/MappingChaining) c
- [mapping inversion-based matching process](https://w3id.org/semapv/vocab/MappingInversion) c
- [semantic similarity threshold-based matching process](https://w3id.org/semapv/vocab/SemanticSimilarityThresholdMatching) c
- [structural matching process](https://w3id.org/semapv/vocab/StructuralMatching) c
- [unspecified matching process](https://w3id.org/semapv/vocab/UnspecifiedMatching) c

### matching process post-processing c

IRI `https://w3id.org/semapv/vocab/MatchingPostProcessing` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A process applied to a set of mappings, usually with the intention of changing it.

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [mapping activity](https://w3id.org/semapv/vocab/MappingActivity) c [Super Class Of](https://w3id.org/profile/ontdoc/superClassOf "Inverse of RDFS' subClassOf. Defined in Ontology Documentation Profile")

- [cardinality filtering](https://w3id.org/semapv/vocab/CardinalityFiltering) c
- [logical consistency filtering](https://w3id.org/semapv/vocab/LogicalConsistencyFiltering) c
- [stable marriage filtering](https://w3id.org/semapv/vocab/StableMarriageFiltering) c
- [threshold filtering](https://w3id.org/semapv/vocab/ThresholdFiltering) c

### matching process pre-processing c

IRI `https://w3id.org/semapv/vocab/MatchingPreprocessing` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A preliminary processing of inputs prior to performing matching.

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [mapping activity](https://w3id.org/semapv/vocab/MappingActivity) c [Super Class Of](https://w3id.org/profile/ontdoc/superClassOf "Inverse of RDFS' subClassOf. Defined in Ontology Documentation Profile") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### normalization c

IRI `https://w3id.org/semapv/vocab/Normalization` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A family of preprocessing techniques for reducing strings to be compared to a common format.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process pre-processing](https://w3id.org/semapv/vocab/MatchingPreprocessing) c [Super Class Of](https://w3id.org/profile/ontdoc/superClassOf "Inverse of RDFS' subClassOf. Defined in Ontology Documentation Profile")

- [blank normalisation](https://w3id.org/semapv/vocab/BlankNormalisation) c
- [case normalization](https://w3id.org/semapv/vocab/CaseNormalization) c
- [diacritics suppression](https://w3id.org/semapv/vocab/DiacriticsSuppression) c
- [digit suppression](https://w3id.org/semapv/vocab/DigitSuppression) c
- [lemmatization](https://w3id.org/semapv/vocab/Lemmatization) c
- [link stripping](https://w3id.org/semapv/vocab/LinkStripping) c
- [punctuation elimination](https://w3id.org/semapv/vocab/PunctuationElemination) c
- [regex removal](https://w3id.org/semapv/vocab/RegexRemoval) c
- [regex replacement](https://w3id.org/semapv/vocab/RegexReplacement) c
- [stemming](https://w3id.org/semapv/vocab/Stemming) c
- [stop-word removal](https://w3id.org/semapv/vocab/StopWordRemoval) c
- [term extraction](https://w3id.org/semapv/vocab/TermExtraction) c
- [tokenization](https://w3id.org/semapv/vocab/Tokenization) c

### punctuation elimination c

IRI `https://w3id.org/semapv/vocab/PunctuationElemination` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A normalization technique removing all punctation characters from a string.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
The string 'e.g.' becomes 'eg'.
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### regex removal c

IRI `https://w3id.org/semapv/vocab/RegexRemoval` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A preprocessing method transforming a string by matching a regular expression and then removing that match.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
The regex match “[ -]phenotype” is removed from the label field of the subject entity in the mapping.
```

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### regex replacement c

IRI `https://w3id.org/semapv/vocab/RegexReplacement` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A preprocessing method transforming a string by matching a regular expression and then replacing that match with a specified substitution string.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
The regex match “[ -]phenotype” is replaced by “-disease” for the label field of the subject entity in the mapping.
```

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### semantic similarity threshold-based matching process c

IRI `https://w3id.org/semapv/vocab/SemanticSimilarityThresholdMatching` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A matching process based on a minimum threshold of a score from a comparison based on a semantic similarity algorithm.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
A match between a subject and an object entity was established because they had a Jaccard score higher than 0.8 based on the set of (common) superclasses.
```

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process](https://w3id.org/semapv/vocab/Matching) c

### similarity measure c

IRI `https://w3id.org/semapv/vocab/SimilarityMeasure` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A technique for determining a score that characterises the similarity between two entities.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Super Class Of](https://w3id.org/profile/ontdoc/superClassOf "Inverse of RDFS' subClassOf. Defined in Ontology Documentation Profile")

- [language-based similarity measure](https://w3id.org/semapv/vocab/LanguageBasedSimilarityMeasure) c
- [string-based similarity measure](https://w3id.org/semapv/vocab/StringBasedSimilarityMeasure) c

### stable marriage filtering c

IRI `https://w3id.org/semapv/vocab/StableMarriageFiltering` [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process post-processing](https://w3id.org/semapv/vocab/MatchingPostProcessing) c

### stemming c

IRI `https://w3id.org/semapv/vocab/Stemming` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

The process of reducing a word to its word stem.

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### stop-word removal c

IRI `https://w3id.org/semapv/vocab/StopWordRemoval` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A preprocessing method transforming a string by removing a list of stop words.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
The stop-words “of, and, is, a” are removed from the label field of the subject entity in the mapping.
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### string-based similarity measure c

IRI `https://w3id.org/semapv/vocab/StringBasedSimilarityMeasure` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A similarity measure based on the comparison of strings.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [similarity measure](https://w3id.org/semapv/vocab/SimilarityMeasure) c [Super Class Of](https://w3id.org/profile/ontdoc/superClassOf "Inverse of RDFS' subClassOf. Defined in Ontology Documentation Profile")

- [edit distance](https://w3id.org/semapv/vocab/EditDistance) c
- [hamming distance](https://w3id.org/semapv/vocab/HammingDistance) c
- [string equality](https://w3id.org/semapv/vocab/StringEquality) c
- [substring similarity](https://w3id.org/semapv/vocab/SubstringSimilarity) c
- [substring test](https://w3id.org/semapv/vocab/SubstringTest) c
- [token-based distance](https://w3id.org/semapv/vocab/TokenBasedDistance) c
- [ngram similarity](https://w3id.org/semapv/vocab/nGramSimilarity) c

### string equality c

IRI `https://w3id.org/semapv/vocab/StringEquality` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A string-based similarity measure which involves determining if two strings associated with mapping entities are equal.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [string-based similarity measure](https://w3id.org/semapv/vocab/StringBasedSimilarityMeasure) c

### structural matching process c

IRI `https://w3id.org/semapv/vocab/StructuralMatching` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

Structural matching does not involve looking at "values" of properties.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
A match between a subject and an object was established because of the similarity of their structural features, e.g., the number of direct property of a class.
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1016/j.websem.2009.11.002](https://doi.org/10.1016/j.websem.2009.11.002) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process](https://w3id.org/semapv/vocab/Matching) c

### substring similarity c

IRI `https://w3id.org/semapv/vocab/SubstringSimilarity` [Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [string-based similarity measure](https://w3id.org/semapv/vocab/StringBasedSimilarityMeasure) c

### substring test c

IRI `https://w3id.org/semapv/vocab/SubstringTest` [Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [string-based similarity measure](https://w3id.org/semapv/vocab/StringBasedSimilarityMeasure) c

### term extraction c

IRI `https://w3id.org/semapv/vocab/TermExtraction` [Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### threshold filtering c

IRI `https://w3id.org/semapv/vocab/ThresholdFiltering` [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process post-processing](https://w3id.org/semapv/vocab/MatchingPostProcessing) c

### token-based distance c

IRI `https://w3id.org/semapv/vocab/TokenBasedDistance` [Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [string-based similarity measure](https://w3id.org/semapv/vocab/StringBasedSimilarityMeasure) c

### tokenization c

IRI `https://w3id.org/semapv/vocab/Tokenization` [Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [normalization](https://w3id.org/semapv/vocab/Normalization) c

### unspecified matching process c

IRI `https://w3id.org/semapv/vocab/UnspecifiedMatching` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A matching process based on an unspecified comparison.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
A mapping between a subject and an object was established, but it is no longer clear how or why.
```

[Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [matching process](https://w3id.org/semapv/vocab/Matching) c

### ngram similarity c

IRI `https://w3id.org/semapv/vocab/nGramSimilarity` [Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://doi.org/10.1007/978-3-642-38721-0](https://doi.org/10.1007/978-3-642-38721-0) [Sub Class Of](http://www.w3.org/2000/01/rdf-schema#subClassOf "The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)") [string-based similarity measure](https://w3id.org/semapv/vocab/StringBasedSimilarityMeasure) c

## Annotation Properties

### description ap

IRI `http://purl.org/dc/terms/description`

### license ap

IRI `http://purl.org/dc/terms/license`

### source ap

IRI `http://purl.org/dc/terms/source`

### title ap

IRI `http://purl.org/dc/terms/title`

### alt label ap

IRI `http://www.w3.org/2004/02/skos/core#altLabel`

### broad match ap

IRI `http://www.w3.org/2004/02/skos/core#broadMatch` [Is Defined By](http://www.w3.org/2000/01/rdf-schema#isDefinedBy "The definition of the subject resource. Defined in The RDF Schema vocabulary (RDFS)") [skos:](http://www.w3.org/2004/02/skos/core) [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A match where the object is a broader concept than the subject.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/) [Sub Property Of](http://www.w3.org/2000/01/rdf-schema#subPropertyOf "The subject is a subproperty of a property. Defined in The RDF Schema vocabulary (RDFS)") [non-isomorphic match](https://w3id.org/semapv/vocab/nonIsomorphicMatch) ap [Super Property Of](https://w3id.org/profile/ontdoc/superPropertyOf "Inverse of RDFS' subPropertyOf. Defined in Ontology Documentation Profile") [cross-species broad match](https://w3id.org/semapv/vocab/crossSpeciesBroadMatch) ap

### close match ap

IRI `http://www.w3.org/2004/02/skos/core#closeMatch` [Is Defined By](http://www.w3.org/2000/01/rdf-schema#isDefinedBy "The definition of the subject resource. Defined in The RDF Schema vocabulary (RDFS)") [skos:](http://www.w3.org/2004/02/skos/core) [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A match where the subject and object are sufficiently similar that they can be used interchangeably in some information retrieval applications.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/) [Sub Property Of](http://www.w3.org/2000/01/rdf-schema#subPropertyOf "The subject is a subproperty of a property. Defined in The RDF Schema vocabulary (RDFS)") [is in mapping relation with](http://www.w3.org/2004/02/skos/core#mappingRelation) ap [Super Property Of](https://w3id.org/profile/ontdoc/superPropertyOf "Inverse of RDFS' subPropertyOf. Defined in Ontology Documentation Profile")

- [has exact match](http://www.w3.org/2004/02/skos/core#exactMatch) ap
- [cross-species close match](https://w3id.org/semapv/vocab/crossSpeciesCloseMatch) ap

### definition ap

IRI `http://www.w3.org/2004/02/skos/core#definition`

### exact match ap

IRI `http://www.w3.org/2004/02/skos/core#exactMatch` [Is Defined By](http://www.w3.org/2000/01/rdf-schema#isDefinedBy "The definition of the subject resource. Defined in The RDF Schema vocabulary (RDFS)") [skos:](http://www.w3.org/2004/02/skos/core) [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A match where the subject and object are sufficiently similar, with a high degree of confidence, that they can be used interchangeably across a wide range of information retrieval applications.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/) [Sub Property Of](http://www.w3.org/2000/01/rdf-schema#subPropertyOf "The subject is a subproperty of a property. Defined in The RDF Schema vocabulary (RDFS)")

- [has close match](http://www.w3.org/2004/02/skos/core#closeMatch) ap
- [isomorphic match](https://w3id.org/semapv/vocab/isomorphicMatch) ap

### example ap

IRI `http://www.w3.org/2004/02/skos/core#example`

### mapping relation ap

IRI `http://www.w3.org/2004/02/skos/core#mappingRelation` [Is Defined By](http://www.w3.org/2000/01/rdf-schema#isDefinedBy "The definition of the subject resource. Defined in The RDF Schema vocabulary (RDFS)") [skos:](http://www.w3.org/2004/02/skos/core) [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A mapping (alignment) link between two concepts.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/) [Super Property Of](https://w3id.org/profile/ontdoc/superPropertyOf "Inverse of RDFS' subPropertyOf. Defined in Ontology Documentation Profile")

- [has close match](http://www.w3.org/2004/02/skos/core#closeMatch) ap
- [isomorphic match](https://w3id.org/semapv/vocab/isomorphicMatch) ap
- [non-isomorphic match](https://w3id.org/semapv/vocab/nonIsomorphicMatch) ap

### narrow match ap

IRI `http://www.w3.org/2004/02/skos/core#narrowMatch` [Is Defined By](http://www.w3.org/2000/01/rdf-schema#isDefinedBy "The definition of the subject resource. Defined in The RDF Schema vocabulary (RDFS)") [skos:](http://www.w3.org/2004/02/skos/core) [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A match where the object is a narrower concept that the subject.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/) [Sub Property Of](http://www.w3.org/2000/01/rdf-schema#subPropertyOf "The subject is a subproperty of a property. Defined in The RDF Schema vocabulary (RDFS)") [non-isomorphic match](https://w3id.org/semapv/vocab/nonIsomorphicMatch) ap [Super Property Of](https://w3id.org/profile/ontdoc/superPropertyOf "Inverse of RDFS' subPropertyOf. Defined in Ontology Documentation Profile") [cross-species narrow match](https://w3id.org/semapv/vocab/crossSpeciesNarrowMatch) ap

### pref label ap

IRI `http://www.w3.org/2004/02/skos/core#prefLabel`

### related match ap

IRI `http://www.w3.org/2004/02/skos/core#relatedMatch` [Is Defined By](http://www.w3.org/2000/01/rdf-schema#isDefinedBy "The definition of the subject resource. Defined in The RDF Schema vocabulary (RDFS)") [skos:](http://www.w3.org/2004/02/skos/core) [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A match where the subject and the object are inherently related, but where none is in any way more general than the other.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/) [Sub Property Of](http://www.w3.org/2000/01/rdf-schema#subPropertyOf "The subject is a subproperty of a property. Defined in The RDF Schema vocabulary (RDFS)") [non-isomorphic match](https://w3id.org/semapv/vocab/nonIsomorphicMatch) ap [Super Property Of](https://w3id.org/profile/ontdoc/superPropertyOf "Inverse of RDFS' subPropertyOf. Defined in Ontology Documentation Profile") [cross-species exact match](https://w3id.org/semapv/vocab/crossSpeciesExactMatch) ap

### cross-species broad match ap

IRI `https://w3id.org/semapv/vocab/crossSpeciesBroadMatch` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A match where the subject is considered analogous to the subject in a different taxonomic grouping, but the object refers to a broader concept.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
FBbt:00007091 (D. melanogaster “subperineurial glial sheath”) and UBERON:0000202 (taxon-neutral “glial blood brain barrier”) are a cross-species broad match.
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://github.com/mapping-commons/semantic-mapping-vocabulary/issues/3](https://github.com/mapping-commons/semantic-mapping-vocabulary/issues/3) [Sub Property Of](http://www.w3.org/2000/01/rdf-schema#subPropertyOf "The subject is a subproperty of a property. Defined in The RDF Schema vocabulary (RDFS)") [has broader match](http://www.w3.org/2004/02/skos/core#broadMatch) ap

### cross-species close match ap

IRI `https://w3id.org/semapv/vocab/crossSpeciesCloseMatch` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A match where the subject and the object belong in different taxonomic groupings, but refer to concepts similar enough that they can be used interchangeably.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://github.com/mapping-commons/semantic-mapping-vocabulary/issues/3](https://github.com/mapping-commons/semantic-mapping-vocabulary/issues/3) [Sub Property Of](http://www.w3.org/2000/01/rdf-schema#subPropertyOf "The subject is a subproperty of a property. Defined in The RDF Schema vocabulary (RDFS)")

- [has close match](http://www.w3.org/2004/02/skos/core#closeMatch) ap
- [non-isomorphic match](https://w3id.org/semapv/vocab/nonIsomorphicMatch) ap

### cross-species exact match ap

IRI `https://w3id.org/semapv/vocab/crossSpeciesExactMatch` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A match where the subject is considered analogous to the object in a different taxonomic grouping.

[Example](http://www.w3.org/2004/02/skos/core#example "An example of the use of a concept. Defined in SKOS Vocabulary")

```
FBbt:00005074 (D. melanogaster “muscle cell”) and CL:0000187 (taxon-neutral “muscle cell”) are a cross-species exact match.
```

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://github.com/mapping-commons/semantic-mapping-vocabulary/issues/3](https://github.com/mapping-commons/semantic-mapping-vocabulary/issues/3) [Sub Property Of](http://www.w3.org/2000/01/rdf-schema#subPropertyOf "The subject is a subproperty of a property. Defined in The RDF Schema vocabulary (RDFS)")

- [has related match](http://www.w3.org/2004/02/skos/core#relatedMatch) ap
- [isomorphic match](https://w3id.org/semapv/vocab/isomorphicMatch) ap

### cross-species narrow match ap

IRI `https://w3id.org/semapv/vocab/crossSpeciesNarrowMatch` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A match where the subject is considered analogous to the subject in a different taxonomic grouping, but the object refers to a narrower concept.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://github.com/mapping-commons/semantic-mapping-vocabulary/issues/3](https://github.com/mapping-commons/semantic-mapping-vocabulary/issues/3) [Sub Property Of](http://www.w3.org/2000/01/rdf-schema#subPropertyOf "The subject is a subproperty of a property. Defined in The RDF Schema vocabulary (RDFS)") [has narrower match](http://www.w3.org/2004/02/skos/core#narrowMatch) ap

### isomorphic match ap

IRI `https://w3id.org/semapv/vocab/isomorphicMatch` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A match where the subject is isomorphic to the object, i.e. considered of identical or similar form, shape, or structure.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://github.com/mapping-commons/semantic-mapping-vocabulary/issues/3](https://github.com/mapping-commons/semantic-mapping-vocabulary/issues/3) [Sub Property Of](http://www.w3.org/2000/01/rdf-schema#subPropertyOf "The subject is a subproperty of a property. Defined in The RDF Schema vocabulary (RDFS)") [is in mapping relation with](http://www.w3.org/2004/02/skos/core#mappingRelation) ap [Super Property Of](https://w3id.org/profile/ontdoc/superPropertyOf "Inverse of RDFS' subPropertyOf. Defined in Ontology Documentation Profile")

- [has exact match](http://www.w3.org/2004/02/skos/core#exactMatch) ap
- [cross-species exact match](https://w3id.org/semapv/vocab/crossSpeciesExactMatch) ap

### non-isomorphic match ap

IRI `https://w3id.org/semapv/vocab/nonIsomorphicMatch` [Description](http://purl.org/dc/terms/description "An account of the resource. Defined in DCMI Metadata Terms")

A match where the subject cannot be considered isomorphic to the object, i.e. considered of identical or similar form, shape, or structure. The object corresponds to exactly one subject in the subject\_source.

[Source](http://purl.org/dc/terms/source "A related resource from which the described resource is derived. Defined in DCMI Metadata Terms") [https://github.com/mapping-commons/semantic-mapping-vocabulary/issues/3](https://github.com/mapping-commons/semantic-mapping-vocabulary/issues/3) [Sub Property Of](http://www.w3.org/2000/01/rdf-schema#subPropertyOf "The subject is a subproperty of a property. Defined in The RDF Schema vocabulary (RDFS)") [is in mapping relation with](http://www.w3.org/2004/02/skos/core#mappingRelation) ap [Super Property Of](https://w3id.org/profile/ontdoc/superPropertyOf "Inverse of RDFS' subPropertyOf. Defined in Ontology Documentation Profile")

- [has broader match](http://www.w3.org/2004/02/skos/core#broadMatch) ap
- [has narrower match](http://www.w3.org/2004/02/skos/core#narrowMatch) ap
- [has related match](http://www.w3.org/2004/02/skos/core#relatedMatch) ap
- [cross-species close match](https://w3id.org/semapv/vocab/crossSpeciesCloseMatch) ap

## Namespaces

dcterms

`http://purl.org/dc/terms/`

doi

`https://doi.org/`

ns1

`http://w3id.org/semapv/vocab/`

owl

`http://www.w3.org/2002/07/owl#`

rdf

`http://www.w3.org/1999/02/22-rdf-syntax-ns#`

rdfs

`http://www.w3.org/2000/01/rdf-schema#`

semapv

`https://w3id.org/semapv/`

semapv\_voc

`https://w3id.org/semapv/vocab/`

skos

`http://www.w3.org/2004/02/skos/core#`

## Legend

c Classes ap Annotation Properties

made by [p y LODE](https://github.com/rdflib/pyLODE) [3.1.4](https://github.com/rdflib/pyLODE/release/3.1.4) with the [OntPub](https://w3id.org/profile/ontpub) profile

### Table of Contents

- #### [Metadata](#metadata)
- #### [Classes](#classes)
  
  - [background knowledge-based matching process](#backgroundknowledge-basedmatchingprocess)
  - [blank normalisation](#blanknormalisation)
  - [cardinality filtering](#cardinalityfiltering)
  - [case normalization](#casenormalization)
  - [composite matching process](#compositematchingprocess)
  - [diacritics suppression](#diacriticssuppression)
  - [digit suppression](#digitsuppression)
  - [edit distance](#editdistance)
  - [hamming distance](#hammingdistance)
  - [instance-based matching process](#instance-basedmatchingprocess)
  - [language-based similarity measure](#language-basedsimilaritymeasure)
  - [lemmatization](#lemmatization)
  - [levenshtein distance](#levenshteindistance)
  - [lexical matching process](#lexicalmatchingprocess)
  - [lexical similarity threshold-based matching process](#lexicalsimilaritythreshold-basedmatchingprocess)
  - [link stripping](#linkstripping)
  - [logical consistency filtering](#logicalconsistencyfiltering)
  - [logical reasoning matching process](#logicalreasoningmatchingprocess)
  - [manual mapping curation](#manualmappingcuration)
  - [mapping](#mapping)
  - [mapping activity](#mappingactivity)
  - [mapping chaining-based matching process](#mappingchaining-basedmatchingprocess)
  - [mapping inversion-based matching process](#mappinginversion-basedmatchingprocess)
  - [mapping review](#mappingreview)
  - [matching process](#matchingprocess)
  - [matching process post-processing](#matchingprocesspost-processing)
  - [matching process pre-processing](#matchingprocesspre-processing)
  - [normalization](#normalization)
  - [punctuation elimination](#punctuationelimination)
  - [regex removal](#regexremoval)
  - [regex replacement](#regexreplacement)
  - [semantic similarity threshold-based matching process](#semanticsimilaritythreshold-basedmatchingprocess)
  - [similarity measure](#similaritymeasure)
  - [stable marriage filtering](#stablemarriagefiltering)
  - [stemming](#stemming)
  - [stop-word removal](#stop-wordremoval)
  - [string-based similarity measure](#string-basedsimilaritymeasure)
  - [string equality](#stringequality)
  - [structural matching process](#structuralmatchingprocess)
  - [substring similarity](#substringsimilarity)
  - [substring test](#substringtest)
  - [term extraction](#termextraction)
  - [threshold filtering](#thresholdfiltering)
  - [token-based distance](#token-baseddistance)
  - [tokenization](#tokenization)
  - [unspecified matching process](#unspecifiedmatchingprocess)
  - [ngram similarity](#ngramsimilarity)
- #### [Annotation Properties](#annotationproperties)
  
  - [description](#description)
  - [license](#license)
  - [source](#source)
  - [title](#title)
  - [alt label](#altLabel)
  - [broad match](#broadmatch)
  - [close match](#closematch)
  - [definition](#definition)
  - [exact match](#exactmatch)
  - [example](#example)
  - [mapping relation](#mappingrelation)
  - [narrow match](#narrowmatch)
  - [pref label](#prefLabel)
  - [related match](#relatedmatch)
  - [cross-species broad match](#cross-speciesbroadmatch)
  - [cross-species close match](#cross-speciesclosematch)
  - [cross-species exact match](#cross-speciesexactmatch)
  - [cross-species narrow match](#cross-speciesnarrowmatch)
  - [isomorphic match](#isomorphicmatch)
  - [non-isomorphic match](#non-isomorphicmatch)
- #### [Namespaces](#namespaces)
  
  - [dcterms](#dcterms)
  - [doi](#doi)
  - [ns1](#ns1)
  - [owl](#owl)
  - [rdf](#rdf)
  - [rdfs](#rdfs)
  - [semapv](#semapv)
  - [semapv\_voc](#semapv_voc)
  - [skos](#skos)
- #### [Legend](#legend)
