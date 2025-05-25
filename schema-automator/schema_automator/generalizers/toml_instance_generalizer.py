import click
from typing import Union, Dict, List, Any
from collections import defaultdict
import json
import yaml
import gzip

from dataclasses import dataclass

from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import SchemaDefinition

from schema_automator import JsonDataGeneralizer
from schema_automator.generalizers.generalizer import Generalizer
from schema_automator.generalizers.csv_data_generalizer import CsvDataGeneralizer
from linkml_runtime.utils.formatutils import camelcase

from schema_automator.utils.schemautils import write_schema


@dataclass
class TomlDataGeneralizer(Generalizer):
    """
    A generalizer that abstract from TOML instance data
    """
    mappings: dict = None
    omit_null: bool = None

    def convert(self, input: str, **kwargs) -> SchemaDefinition:
        """
        Generalizes from a JSON file

        :param input:
        :param kwargs:
        :return:
        """
        w
        json_engine = JsonDataGeneralizer(**kwargs)
        return json_engine.convert(input, format='toml', **kwargs)



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
        