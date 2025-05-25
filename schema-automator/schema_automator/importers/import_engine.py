from abc import ABC
from dataclasses import dataclass

from linkml_runtime.linkml_model import SchemaDefinition, Prefix


@dataclass
class ImportEngine(ABC):
    """
    Abstract Base Class for all Import Engines.

    Import Engines take some kind of input and import into a new SchemaDefinition
    """

    def convert(self, file: str, **kwargs) -> SchemaDefinition:
        raise NotImplementedError

    def add_prefix(self, schema: SchemaDefinition, prefix: str, url: str):
        schema.prefixes[prefix] = Prefix(prefix, url)

    def add_default_prefixes(self, schema: SchemaDefinition):
        self.add_prefix(schema, 'linkml', 'https://w3id.org/linkml/')


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
        