"""
See https://github.com/geneontology/obographs
"""


class OboGraph:

    nodemap = {}

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        return


class Node:
    def __init__(self, id, label=None, meta=None, **args):    
        self.id = id
        self.label = label
        self.meta = meta
        if 'lbl' in args:
            self.label = args['lbl']

    def __str__(self):
        return self.id+' "'+str(self.label)+'"'


class Edge:
    def __init__(self, sub, pred, obj, meta=None):    
        self.sub = sub
        self.pred = pred
        self.obj = obj
    
    def __str__(self):
        return self.sub +"-["+self.pred+"]->"+self.obj


class Meta:
    def __init__(self, obj=None):
        if obj is None:
            obj = {}
        self.type_list = obj['types']
        self.category_list = []
        if 'category' in obj:
            self.category_list = obj['category']
        self.pmap = obj



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
