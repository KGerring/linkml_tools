#!/usr/bin/env python3

import rdflib
from rdflib import RDF as rdf, RDFS as rdfs

__all__ = [
    'dc',
    'dcterms',
    'oboInOwl',
    'owl',
    'prov',
    'rdf',
    'rdfs',
    'skos',
    'npoph',
]

###

dc = rdflib.namespace.ClosedNamespace(
    uri=rdflib.URIRef('http://purl.org/dc/elements/1.1/'),
    terms=['contributor',
           'coverage',
           'creator',
           'date',
           'description',
           'format',
           'identifier',
           'language',
           'publisher',
           'relation',
           'rights',
           'source',
           'subject',
           'title',
           'type']
)

dcterms = rdflib.namespace.ClosedNamespace(
    uri=rdflib.URIRef('http://purl.org/dc/terms/'),
    terms=['Agent',
           'AgentClass',
           'BibliographicResource',
           'Box',
           'DCMIType',
           'DDC',
           'FileFormat',
           'Frequency',
           'IMT',
           'ISO3166',
           'ISO639-2',
           'ISO639-3',
           'Jurisdiction',
           'LCC',
           'LCSH',
           'LicenseDocument',
           'LinguisticSystem',
           'Location',
           'LocationPeriodOrJurisdiction',
           'MESH',
           'MediaType',
           'MediaTypeOrExtent',
           'MethodOfAccrual',
           'MethodOfInstruction',
           'NLM',
           'Period',
           'PeriodOfTime',
           'PhysicalMedium',
           'PhysicalResource',
           'Point',
           'Policy',
           'ProvenanceStatement',
           'RFC1766',
           'RFC3066',
           'RFC4646',
           'RFC5646',
           'RightsStatement',
           'SizeOrDuration',
           'Standard',
           'TGN',
           'UDC',
           'URI',
           'W3CDTF',
           'abstract',
           'accessRights',
           'accrualMethod',
           'accrualPeriodicity',
           'accrualPolicy',
           'alternative',
           'audience',
           'available',
           'bibliographicCitation',
           'conformsTo',
           'contributor',
           'coverage',
           'created',
           'creator',
           'date',
           'dateAccepted',
           'dateCopyrighted',
           'dateSubmitted',
           'description',
           'educationLevel',
           'extent',
           'format',
           'hasFormat',
           'hasPart',
           'hasVersion',
           'identifier',
           'instructionalMethod',
           'isFormatOf',
           'isPartOf',
           'isReferencedBy',
           'isReplacedBy',
           'isRequiredBy',
           'isVersionOf',
           'issued',
           'language',
           'license',
           'mediator',
           'medium',
           'modified',
           'provenance',
           'publisher',
           'references',
           'relation',
           'replaces',
           'requires',
           'rights',
           'rightsHolder',
           'source',
           'spatial',
           'subject',
           'tableOfContents',
           'temporal',
           'title',
           'type',
           'valid']
)

npoph = rdflib.namespace.ClosedNamespace(
    uri=rdflib.URIRef('http://uri.interlex.org/tgbugs/uris/readable/'),
    terms=['NeuronCUT',
           'NeuronEBM',
           'Phenotype',
           'delineates',
           'hasAxonLocatedIn',
           'hasAxonMorphologicalPhenotype',
           'hasAxonPhenotype',
           'hasAxonPresynapticElementIn',
           'hasBiologicalSex',
           'hasCircuitRolePhenotype',
           'hasClassificationPhenotype',
           'hasComputedMolecularPhenotype',
           'hasComputedMolecularPhenotypeFromDNA',
           'hasComputedMolecularPhenotypeFromProtein',
           'hasComputedMolecularPhenotypeFromRNA',
           'hasComputedPhenotype',
           'hasConnectionDeterminedByCellFilling',
           'hasConnectionDeterminedByElectronMicroscopy',
           'hasConnectionDeterminedByElectrophysiology',
           'hasConnectionDeterminedByPharmacology',
           'hasConnectionDeterminedBySynapticPhysiology',
           'hasConnectionDeterminedByViralTracing',
           'hasConnectionPhenotype',
           'hasDendriteLocatedIn',
           'hasDendriteMorphologicalPhenotype',
           'hasDendritePhenotype',
           'hasDevelopmentalStage',
           'hasDevelopmentalStructure',
           'hasDevelopmentalType',
           'hasDriverExpressionConstitutivePhenotype',
           'hasDriverExpressionInducedPhenotype',
           'hasDriverExpressionPhenotype',
           'hasElectrophysiologicalPhenotype',
           'hasExperimentalPhenotype',
           'hasExpressionPhenotype',
           'hasForwardConnectionPhenotype',
           'hasInstanceInSpecies',
           'hasInstanceInTaxon',
           'hasLayerLocationPhenotype',
           'hasLocationPhenotype',
           'hasMolecularPhenotype',
           'hasMorphologicalPhenotype',
           'hasNeurotransmitterPhenotype',
           'hasNucleicAcidExpressionPhenotype',
           'hasPhenotype',
           'hasPhenotypeModifier',
           'hasPresynapticElementIn',
           'hasPresynapticTerminalsIn',
           'hasProcessLocatedIn',
           'hasProjectionPhenotype',
           'hasProteinExpressionPhenotype',
           'hasReporterExpressionPhenotype',
           'hasReverseConnectionPhenotype',
           'hasSmallMoleculePhenotype',
           'hasSomaLocatedIn',
           'hasSomaLocatedInLayer',
           'hasSomaLocationLaterality',
           'hasSomaPhenotype',
           'hasTaxonRank',
           'phenotypeCooccuresWith',
           'phenotypeObservedInBrainRegion',
           'phenotypeOf']
)

oboInOwl = rdflib.namespace.ClosedNamespace(
    uri=rdflib.URIRef('http://www.geneontology.org/formats/oboInOwl#'),
    terms=['DbXref',
           'Definition',
           'ObsoleteClass',
           'ObsoleteProperty',
           'Subset',
           'SubsetProperty',
           'Synonym',
           'SynonymType',
           'SynonymTypeProperty',
           'consider',
           'hasAlternativeId',
           'hasBroadSynonym',
           'hasDate',
           'hasDbXref',
           'hasDefaultNamespace',
           'hasDefinition',
           'hasExactSynonym',
           'hasNarrowSynonym',
           'hasOBONamespace',
           'hasRelatedSynonym',
           'hasSubset',
           'hasSynonym',
           'hasSynonymType',
           'hasURI',
           'hasVersion',
           'inSubset',
           'isCyclic',
           'replacedBy',
           'savedBy']
)

owl = rdflib.namespace.ClosedNamespace(
    uri=rdflib.URIRef('http://www.w3.org/2002/07/owl#'),
    terms=['AllDifferent',
           'AllDisjointClasses',
           'AllDisjointProperties',
           'Annotation',
           'AnnotationProperty',
           'AsymmetricProperty',
           'Axiom',
           'Class',
           'DataRange',
           'DatatypeProperty',
           'DeprecatedClass',
           'DeprecatedProperty',
           'FunctionalProperty',
           'InverseFunctionalProperty',
           'IrreflexiveProperty',
           'NamedIndividual',
           'NegativePropertyAssertion',
           'Nothing',
           'ObjectProperty',
           'Ontology',
           'OntologyProperty',
           'ReflexiveProperty',
           'Restriction',
           'SymmetricProperty',
           'Thing',
           'TransitiveProperty',
           'allValuesFrom',
           'annotatedProperty',
           'annotatedSource',
           'annotatedTarget',
           'assertionProperty',
           'backwardCompatibleWith',
           'bottomDataProperty',
           'bottomObjectProperty',
           'cardinality',
           'complementOf',
           'datatypeComplementOf',
           'deprecated',
           'differentFrom',
           'disjointUnionOf',
           'disjointWith',
           'distinctMembers',
           'equivalentClass',
           'equivalentProperty',
           'hasKey',
           'hasSelf',
           'hasValue',
           'imports',
           'incompatibleWith',
           'intersectionOf',
           'inverseOf',
           'maxCardinality',
           'maxQualifiedCardinality',
           'members',
           'minCardinality',
           'minQualifiedCardinality',
           'onClass',
           'onDataRange',
           'onDatatype',
           'onProperties',
           'onProperty',
           'oneOf',
           'priorVersion',
           'propertyChainAxiom',
           'propertyDisjointWith',
           'qualifiedCardinality',
           'sameAs',
           'someValuesFrom',
           'sourceIndividual',
           'targetIndividual',
           'targetValue',
           'topDataProperty',
           'topObjectProperty',
           'unionOf',
           'versionIRI',
           'versionInfo',
           'withRestrictions']
)

prov = rdflib.namespace.ClosedNamespace(
    uri=rdflib.URIRef('http://www.w3.org/ns/prov#'),
    terms=['Accept',
           'Activity',
           'ActivityInfluence',
           'Agent',
           'AgentInfluence',
           'Association',
           'Attribution',
           'Bundle',
           'Collection',
           'Communication',
           'Contribute',
           'Contributor',
           'Copyright',
           'Create',
           'Creator',
           'Delegation',
           'Derivation',
           'Dictionary',
           'DirectQueryService',
           'EmptyCollection',
           'EmptyDictionary',
           'End',
           'Entity',
           'EntityInfluence',
           'Generation',
           'Influence',
           'Insertion',
           'InstantaneousEvent',
           'Invalidation',
           'KeyEntityPair',
           'Location',
           'Modify',
           'Organization',
           'Person',
           'Plan',
           'PrimarySource',
           'Publish',
           'Publisher',
           'Quotation',
           'Removal',
           'Replace',
           'Revision',
           'RightsAssignment',
           'RightsHolder',
           'Role',
           'ServiceDescription',
           'SoftwareAgent',
           'Start',
           'Submit',
           'Usage',
           'actedOnBehalfOf',
           'activity',
           'activityOfInfluence',
           'agent',
           'agentOfInfluence',
           'alternateOf',
           'aq',
           'asInBundle',
           'atLocation',
           'atTime',
           'category',
           'component',
           'constraints',
           'contributed',
           'definition',
           'derivedByInsertionFrom',
           'derivedByRemovalFrom',
           'describesService',
           'dictionary',
           'dm',
           'editorialNote',
           'editorsDefinition',
           'ended',
           'endedAtTime',
           'entity',
           'entityOfInfluence',
           'generalizationOf',
           'generated',
           'generatedAsDerivation',
           'generatedAtTime',
           'hadActivity',
           'hadDelegate',
           'hadDerivation',
           'hadDictionaryMember',
           'hadGeneration',
           'hadInfluence',
           'hadMember',
           'hadPlan',
           'hadPrimarySource',
           'hadRevision',
           'hadRole',
           'hadUsage',
           'has_anchor',
           'has_provenance',
           'has_query_service',
           'influenced',
           'influencer',
           'informed',
           'insertedKeyEntityPair',
           'invalidated',
           'invalidatedAtTime',
           'inverse',
           'locationOf',
           'mentionOf',
           'n',
           'order',
           'pairEntity',
           'pairKey',
           'pingback',
           'provenanceUriTemplate',
           'qualifiedAssociation',
           'qualifiedAssociationOf',
           'qualifiedAttribution',
           'qualifiedAttributionOf',
           'qualifiedCommunication',
           'qualifiedCommunicationOf',
           'qualifiedDelegation',
           'qualifiedDelegationOf',
           'qualifiedDerivation',
           'qualifiedDerivationOf',
           'qualifiedEnd',
           'qualifiedEndOf',
           'qualifiedForm',
           'qualifiedGeneration',
           'qualifiedGenerationOf',
           'qualifiedInfluence',
           'qualifiedInfluenceOf',
           'qualifiedInsertion',
           'qualifiedInvalidation',
           'qualifiedInvalidationOf',
           'qualifiedPrimarySource',
           'qualifiedQuotation',
           'qualifiedQuotationOf',
           'qualifiedRemoval',
           'qualifiedRevision',
           'qualifiedSourceOf',
           'qualifiedStart',
           'qualifiedStartOf',
           'qualifiedUsage',
           'qualifiedUsingActivity',
           'quotedAs',
           'removedKey',
           'revisedEntity',
           'sharesDefinitionWith',
           'specializationOf',
           'started',
           'startedAtTime',
           'todo',
           'unqualifiedForm',
           'used',
           'value',
           'wasActivityOfInfluence',
           'wasAssociateFor',
           'wasAssociatedWith',
           'wasAttributedTo',
           'wasDerivedFrom',
           'wasEndedBy',
           'wasGeneratedBy',
           'wasInfluencedBy',
           'wasInformedBy',
           'wasInvalidatedBy',
           'wasMemberOf',
           'wasPlanOf',
           'wasPrimarySourceOf',
           'wasQuotedFrom',
           'wasRevisionOf',
           'wasRoleIn',
           'wasStartedBy',
           'wasUsedBy',
           'wasUsedInDerivation']
)

skos = rdflib.namespace.ClosedNamespace(
    uri=rdflib.URIRef('http://www.w3.org/2004/02/skos/core#'),
    terms=['Collection',
           'Concept',
           'ConceptScheme',
           'OrderedCollection',
           'altLabel',
           'broadMatch',
           'broader',
           'broaderTransitive',
           'changeNote',
           'closeMatch',
           'definition',
           'editorialNote',
           'exactMatch',
           'example',
           'hasTopConcept',
           'hiddenLabel',
           'historyNote',
           'inScheme',
           'mappingRelation',
           'member',
           'memberList',
           'narrowMatch',
           'narrower',
           'narrowerTransitive',
           'notation',
           'note',
           'prefLabel',
           'related',
           'relatedMatch',
           'scopeNote',
           'semanticRelation',
           'topConceptOf']
)

###

def main():
    from rdflib.plugin import PluginException
    from rdflib.plugins.parsers.notation3 import BadSyntax
    from urllib.error import URLError

    # use to populate terms
    uris = {
        'oboInOwl': 'http://www.geneontology.org/formats/oboInOwl#',
        'owl': 'http://www.w3.org/2002/07/owl#',
        'skos': 'http://www.w3.org/2004/02/skos/core#',
        'dc': ('https://www.dublincore.org/specifications/dublin-core/'
               'dcmi-terms/dublin_core_elements.ttl'),
        'dcterms': ('https://dublincore.org/specifications/dublin-core/'
                    'dcmi-terms/dublin_core_terms.ttl'),
        'prov': 'http://www.w3.org/ns/prov#',
        'npoph': ('https://raw.githubusercontent.com/SciCrunch/NIF-Ontology/'
                  'neurons/ttl/phenotype-core.ttl'),
    }
    alternate_prefixs = {
        'dc': 'http://purl.org/dc/elements/1.1/',  # no longer fetches correctly
        'dcterms': 'http://purl.org/dc/terms/',  # paul has 308ed the purls
        'npoph': 'http://uri.interlex.org/tgbugs/uris/readable/',
    }
    tw = 4
    tab = ' ' * tw
    ind = ' ' * (tw + len('terms=['))
    functions = ''
    for name, uri in sorted(uris.items()):
        print(uri)
        if uri.endswith('.ttl'):
            args_list = [
                ((uri,), {'format': 'turtle'}),
            ]

        else:
            args_list = [
                ((uri.rstrip('#'),), {}),
                ((uri.rstrip('#') + '.owl',), {}),
                ((uri.rstrip('#') + '.owl',), {'format': 'xml'}),
            ]

        for args, kwargs in args_list:
            try:
                g = rdflib.Graph().parse(*args, **kwargs)
                break
            except PluginException:
                continue
            except BadSyntax:
                continue
            except URLError as e:
                raise URLError(args[0]) from e

        if name in alternate_prefixs:
            uri = alternate_prefixs[name]

        sep = uri[-1]
        globals().update(locals())
        terms = sorted(set(s.rsplit(sep, 1)[-1]
                           for s in g.subjects()
                           if uri in s and uri != s.toPython() and sep in s))
        block = ('\n'
                 '{name} = rdflib.namespace.ClosedNamespace(\n'
                 "{tab}uri=rdflib.URIRef('{uri}'),\n"
                 '{tab}' + "terms=['{t}',\n".format(t=terms[0]) + ''
                 '{ind}' + ',\n{ind}'.join("'{t}'".format(t=t)  # beware order of operations issues
                                           for t in terms[1:]) + ']\n'
                 ')\n')
        function = block.format(name=name,
                                uri=uri,
                                tab=tab,
                                ind=ind)
        functions += function

    functions += '\n'

    with open(__file__, 'rt') as f:
        text = f.read()

    sep = '###\n'
    start, mid, end = text.split(sep)
    code = sep.join((start, functions, end))
    with open(__file__, 'wt') as f:
        f.write(code)

__all__ = sorted(
    [
        getattr(v, "__name__", k)
        for k, v in list(globals().items())  # export
        if (
            (
                callable(v)
                and getattr(v, "__module__", "")
                == __name__  # callables from this module
                or k.isupper()
            )
            and not str(getattr(v, "__name__", k)).startswith("__")  # or CONSTANTS
        )
    ]
)  # neither marked internal


if __name__ == '__main__':
    main()
