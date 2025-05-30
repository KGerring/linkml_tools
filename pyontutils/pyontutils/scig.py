#!/usr/bin/env python3
"""Look look up ontology terms on the command line.

Usage:
    scig v    [--api=A --local --verbose --key=KEY] <id>...
    scig i    [--api=A --local --verbose --key=KEY] <id>...
    scig t    [--api=A --local --verbose --limit=LIMIT --key=KEY --prefix=P...] <term>...
    scig s    [--api=A --local --verbose --limit=LIMIT --key=KEY --prefix=P...] <term>...
    scig g    [--api=A --local --verbose --rt=RELTYPE --edges --key=KEY] <id>...
    scig e    [--api=A --local --verbose --key=KEY] <p> <s> <o>
    scig c    [--api=A --local --verbose --key=KEY]
    scig cy   [--api=A --local --verbose --limit=LIMIT] <query>
    scig onts [--api=A --local --verbose --key=KEY]

Options:
    -a --api=A          Full url to SciGraph api endpoint
    -e --edges          print edges only
    -l --local          hit the local scigraph server
    -v --verbose        print the full uri
    -t --limit=LIMIT    limit number of results [default: 10]
    -k --key=KEY        api key
    -w --warn           warn on errors
    -p --prefix=P       filter by prefix
    -r --rt=RELTYPE     relationshipType

"""
import tempfile
from pathlib import Path
import htmlfn as hfn
from docopt import docopt
from pyontutils.utils_fast import TermColors as tc, getSourceLine, UTCNOWISO
from pyontutils.curies import PREFIXES


def makeProv(pred, root, wgb):
    return [hfn.titletag(f'Transitive closure of {root} under {pred}'),
            f'<meta name="date" content="{UTCNOWISO()}">',
            f'<link rel="http://www.w3.org/ns/prov#wasGeneratedBy" href="{wgb}">']


class ImportChain:  # TODO abstract this a bit to support other onts, move back to pyontutils
    def __init__(self, sgg, sgc, wasGeneratedBy='FIXME#L{line}'):
        self.sgg = sgg
        self.sgc = sgc
        self.wasGeneratedBy = wasGeneratedBy

    def get_scigraph_onts(self):
        self.results = self.sgc.execute('MATCH (n:Ontology) RETURN n', 1000)
        return self.results

    def get_itrips(self, root=None, extras=tuple()):
        import rdflib
        from pyontutils.core import OntId
        from pyontutils.utils import Async, deferred
        results = self.get_scigraph_onts()
        iris = sorted(set(r['iri'] for r in results))
        gin = lambda i: (i, self.sgg.getNeighbors(i, relationshipType='isDefinedBy',
                                                  direction='OUTGOING'))
        iblobs = Async()(deferred(gin)(i) for i in iris)
        imports = [(i, *[(e['obj'], 'owl:imports', e['sub'])
                         for e in blob['edges']
                         if not e['sub'].startswith('_:')])
                   for i, blob in iblobs if blob]
        if root:
            if not extras:
                _subs = set(e['sub']
                            for i, blob in iblobs if blob
                            for e in blob['edges']
                            if not e['sub'].startswith('_:'))
                _objs = set(e['obj']
                            for i, blob in iblobs if blob
                            for e in blob['edges']
                            if not e['sub'].startswith('_:'))
                extras = sorted(_objs - _subs)

            imports.append(
                (root,
                 *[(root, 'owl:imports', extra)
                   for extra in extras]))

        self.itrips = sorted(set(tuple(rdflib.URIRef(OntId(e).iri) for e in t)
                                 for i, *ts in imports if ts for t in ts))

        return self.itrips, extras

    def make_import_chain(self, root='TEMP:NIF-SCIGRAPH-ROOT',
                          ontologies=tuple()):
        from pyontutils.core import OntGraph
        from pyontutils.ontload import import_tree
        itrips, extras = self.get_itrips(root, ontologies)
        if not ontologies:
            ontologies = extras

        if len(extras) == 1:
            root, = extras

        if not [ontology for ontology in
                [o.split(':')[-1] for o in ontologies]
                if any(ontology in t[0] for t in itrips)]:
            return None, None

        import_graph = OntGraph()
        [import_graph.add(t) for t in itrips]

        self.tree, self.extra = import_tree(import_graph, root)
        return self.tree, self.extra

    def make_html(self):
        line = getSourceLine(self.__class__)
        wgb = self.wasGeneratedBy.format(line=line)
        tree, extra  = self.make_import_chain()
        prov = makeProv('owl:imports', 'SCIGRAPH-IMPORT-ROOT', wgb)
        if tree is None:
            html_all = ''
        else:
            html = extra.html.replace('NIFTTL:', '')
            html_all = hfn.htmldoc(html,
                                   other=prov,
                                   styles=hfn.tree_styles)

        self.html = html_all
        return html_all

    def write_import_chain(self, location=tempfile.tempdir):
        html = self.make_html()
        if not html:
            self.path = Path(tempfile.tempdir) / 'noimport.html'
        else:
            self.name = Path(next(iter(self.tree.keys()))).name
            self.path = Path(location, f'{self.name}-import-closure.html')

        with open(self.path.as_posix(), 'wt') as f:
            f.write(html)  # much more readable


class scigPrint:

    _shorten_ = {
        'PR':'http://purl.obolibrary.org/obo/PR_',
        'RO':'http://purl.obolibrary.org/obo/RO_',
        'dc':'http://purl.org/dc/elements/1.1/',
        'BFO':'http://purl.obolibrary.org/obo/BFO_',
        'owl':'http://www.w3.org/2002/07/owl#',
        'rdfs':'http://www.w3.org/2000/01/rdf-schema#',
        'skos':'http://www.w3.org/2004/02/skos/core#',
        'NIFGA':'http://ontology.neuinfo.org/NIF/BiomaterialEntities/NIF-GrossAnatomy.owl#',
        'OBOANN':'http://ontology.neuinfo.org/NIF/Backend/OBO_annotation_properties.owl#',  # FIXME needs to die a swift death
        'oboInOwl':'http://www.geneontology.org/formats/oboInOwl#',
        'NIFSTD':'http://uri.neuinfo.org/nif/nifstd/',
        'NLX':'http://uri.neuinfo.org/nif/nifstd/nlx_',
        'SAO':'http://uri.neuinfo.org/nif/nifstd/sao',
        'BIRNLEX':'http://uri.neuinfo.org/nif/nifstd/birnlex_',
        'NIFRID':'http://uri.neuinfo.org/nif/nifstd/readable/',
        'NIFSUB':'http://ontology.neuinfo.org/NIF/BiomaterialEntities/NIF-Subcellular.owl#',
        'ro':'http://www.obofoundry.org/ro/ro.owl#',
        'UBERON':'http://purl.obolibrary.org/obo/UBERON_',
        'BIRNANN':'http://ontology.neuinfo.org/NIF/Backend/BIRNLex_annotation_properties.owl#',
        'NCBITaxon':'http://purl.obolibrary.org/obo/NCBITaxon_',
        'BRAINInfo':'http://braininfo.rprc.washington.edu/centraldirectory.aspx?ID=',
        'PMID':'http://www.ncbi.nlm.nih.gov/pubmed/',
        'googledocs':'https://docs.google.com/document/d/',
        'googlesheets':'https://docs.google.com/spreadsheet/',
    }
    _shorten_.update(PREFIXES)

    shorten = {v:k for k, v in _shorten_.items()}

    @staticmethod
    def wrap(string, start, ind, wrap_=80):  # FIXME protcur core has an impl
        if len(string) + start <= wrap_:
            return string
        else:
            out = ''
            string = string.replace('\n', ' ')
            string = string.replace('\\n', ' ')
            words = string.split(' ')
            nwords = len(words)
            word_lens = [len(word) for word in words]
            valid_ends = [sum(word_lens[:i + 1]) + i
                          for i, l in enumerate(word_lens)]
            def valid(e):
                if valid_ends[0] >= e:
                    return valid_ends[0]
                li, low = [(i, ve) for i, ve in enumerate(valid_ends) if ve < e][-1]
                hi, high = [(i, ve) for i, ve in enumerate(valid_ends) if ve >= e][0]
                use_low = e - low < high - e
                ind = (li if use_low else hi)
                if ind < nwords - 1:
                    wlp1 = word_lens[ind + 1]
                else:
                    wlp1 = True

                adjust = 1 if not wlp1 else 0

                return (low if use_low else high) + adjust

            ends = [valid(e)  # note, ideally we would adjust to the longest passing block in the fly
                    for e in range(wrap_ - start,
                                   len(string), wrap_ - ind - 4)] + [None]
            starts = [0] + [e for e in ends]
            blocks = [string[s:e] if e else string[s:] for s, e in zip(starts, ends)]
            return ('\n' + ' ' * (ind + 4)).join(blocks)

    @staticmethod
    def sv(asdf, start, ind, warn=False):
        if type(asdf) not in (bool, int, float) and asdf.startswith('http'):  # FIXME why are we not using isinstace(i, str) here?
            for iri, short in scigPrint.shorten.items():
                if iri in asdf:
                    return scigPrint.wrap(asdf.replace(iri, short + ':'), start, ind)
            print(tc.red('WARNING:'), 'Shorten failed for', tc.ltyellow(asdf))
            return scigPrint.wrap(repr(asdf), start, ind)
        else:
            return scigPrint.wrap(repr(asdf), start, ind)

    @staticmethod
    def pprint_node(node):
        nodes = node['nodes']
        if not nodes:
            return  # no node... probably put a None into SciGraph
        else:
            node = nodes[0]  # no edges here...
        print('---------------------------------------------------')
        print(node['id'], '  ', node['lbl'])
        print()
        scigPrint.pprint_meta(node['meta'], False)
        print('---------------------------------------------------')

    @staticmethod
    def pprint_meta(meta, print_iri=True):
        from pyontutils.core import qname
        if print_iri:
            if 'curie' in meta:
                print(meta['curie'])
            else:
                p = qname(meta['iri'])
                if p == meta['iri']:
                    for iri, short in scigPrint.shorten.items():
                        if iri in p:
                            p = p.replace(iri, short + ':')
                            break
                print()
                print(tc.blue(p))

        for k, v in sorted(meta.items()):
            if k in ('curie', 'iri'):
                continue
            for iri, short in scigPrint.shorten.items():
                if iri in k:
                    k = k.replace(iri, short + ':')
                    break
            if v is not None:
                shift = 10 if len(k) <= 10 else (20 if len(k) <= 20 else 30)
                base = ' ' * 4 + f'{k:<{shift}}'
                if isinstance(v, list):
                    if len(v) > 1:
                        print(base, '[')
                        _ = [print(' ' * 8 + scigPrint.sv(_, 8, 8)) for _ in v]
                        print(' ' * 4 + ']')
                    elif len(v) == 1:
                        asdf = v[0]
                        print(base, scigPrint.sv(asdf, len(base) + 1, len(base) - 3))
                    else:
                        pass
                else:
                    print(base, scigPrint.sv(v, len(base) + 1, len(base) - 3))

    @staticmethod
    def pprint_edge(edge):
        def fix(value):
            for iri, short in scigPrint.shorten.items():
                if iri in value:
                    return value.replace(iri, short + ':')
            return value

        e = {k:fix(v) for k, v in edge.items()}
        print('({pred} {sub} {obj}) ; {meta}'.format(**e))

    @staticmethod
    def pprint_neighbors(result, nodes=True):
        if nodes:
            print('\tnodes')
            for node in sorted(result['nodes'], key = lambda n: n['id']):
                scigPrint.pprint_node({'nodes':[node]})
        print('\tedges')
        for edge in sorted(result['edges'], key = lambda e: e['pred']):
            scigPrint.pprint_edge(edge)


def main():
    import pyontutils.scigraph as sg
    args = docopt(__doc__, version='scig 0')
    #print(args)
    server = None
    verbose = False
    if args['--api']:
        server = args['--api']
    if args['--local']:
        server = 'http://localhost:9000/scigraph'
    if args['--verbose']:
        verbose = True
    if args['--key']:
        restService.api_key = args['--key']

    kwargs = {}
    if args['--prefix']:
        kwargs['prefix'] = args['--prefix']

    if args['i'] or args['v']:
        v = sg.Vocabulary(server, verbose) if server else sg.Vocabulary(verbose=verbose)
        for id_ in args['<id>']:
            out = v.findById(id_, **kwargs)
            if out:
                print(id_,)
                for key, value in sorted(out.items()):
                    print('\t%s:' % key, value)
    elif args['s'] or args['t']:
        v = sg.Vocabulary(server, verbose) if server else sg.Vocabulary(verbose=verbose)
        for term in args['<term>']:
            print(term)
            limit = args['--limit']
            out = v.searchByTerm(term, limit=limit, **kwargs) if args['s'] else v.findByTerm(term, limit=limit, **kwargs)
            if out:
                for resp in sorted(out, key=lambda t: t['labels'][0] if t['labels'] else 'zzzzzzzzz'):
                    try:
                        curie = resp.pop('curie')
                    except KeyError:
                        curie = resp.pop('iri')  # GRRRRRRRRRRRRRR
                    print('\t%s' % curie)
                    for key, value in sorted(resp.items()):
                        print('\t\t%s:' % key, value)
                print()
    elif args['g']:
        g = sg.Graph(server, verbose) if server else sg.Graph(verbose=verbose)
        for id_ in args['<id>']:
            out = g.getNeighbors(id_, relationshipType=args['--rt'])
            if out:
                print(id_,)
                scigPrint.pprint_neighbors(out, nodes=not args['--edges'])
    elif args['e']:
        v = sg.Vocabulary(server, verbose) if server else sg.Vocabulary(verbose=verbose)
        p, s, o = args['<p>'], args['<s>'], args['<o>']
        def getl(e):
            r = v.findById(e)
            if r and r['labels']:
                return r['labels'][0]
            else:
                return e

        if ':' in p:
            p = getl(p)
        if ':' in s:
            s = getl(s)
        if ':' in o:
            o = getl(o)

        print('(%s %s %s)' % tuple([_.replace(' ', '-') for _ in (p, s, o)]))
    elif args['c']:
        c = sg.Cypher(server, verbose) if server else sg.Cypher(verbose=verbose)
        curies = c.getCuries()
        align = max([len(c) for c in curies]) + 2
        fmt = '{: <%s}' % align
        for curie, iri in sorted(curies.items()):
            print(fmt.format(repr(curie)), repr(iri))
    elif args['cy']:
        c = sg.Cypher(server, verbose) if server else sg.Cypher(verbose=verbose)
        import pprint
        #results = c.execute(args['<query>'], args['--limit'])
        results = c.execute(args['<query>'], args['--limit'], 'application/json')
        if results:
            import json
            s = json.dumps(results, indent=4)
            print(s)
            #pprint.pprint(results)
        else:
            print('Error?')
    elif args['onts']:
        sgc = sg.Cypher(server, verbose) if server else sg.Cypher(verbose=verbose)
        sgg = sg.Graph(server, verbose) if server else sg.Graph(verbose=verbose)
        ic = ImportChain(sgg, sgc)
        ic.write_import_chain()
        fields = ('iri', 'rdfs:label', 'dc:title', 'definition', 'skos:definition',
                  'rdfs:comment', 'dc:publisher')
        for r in ic.results:
            scigPrint.pprint_meta(r)
            continue
            if len(r) > 1:
                for field in fields:
                    value = r.get(field, '')
                    if value:
                        print(f'{field: <20}{value}')
                print()

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
