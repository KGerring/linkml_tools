
def materialize_xrefs_as_edges(ont, xref_graph=None):
    if xref_graph is None:
        xref_graph = ont.xref_graph
    for (x,y) in xref_graph.edges(data=True):
        nodes = ont.nodes()
        if x in nodes and y in nodes:
            ont.add_parent(x,y,'xref')
            ont.add_parent(y,x,'xref')





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
