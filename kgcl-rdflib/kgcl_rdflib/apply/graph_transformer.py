"""KGCL Graph Transformer."""
import logging
from typing import List

import rdflib
from kgcl_schema.datamodel.kgcl import Change

from .kgcl_2_sparql import convert


def apply_patch(kgcl_instances: List[Change], graph: rdflib.Graph) -> None:
    """Apply patch."""
    for i in kgcl_instances:
        query = convert(i)
        logging.info(f"Query: {query}")
        graph.update(query)


def apply_command(kgcl_instance: Change, graph: rdflib.Graph):
    """Apply command."""
    query = convert(kgcl_instance)
    graph.update(query)


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

