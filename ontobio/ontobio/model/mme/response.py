"""
MME response object, see
https://github.com/ga4gh/mme-apis/blob/87f615/search-api.md
"""

from dataclasses import dataclass, field
from typing import List

from ontobio.model.mme.request import Patient


@dataclass
class Score:
    patient: int


@dataclass
class Result:
    score: Score
    patient: Patient = None
    _disease: str = None
    _disease_label: str = None
    _gene: str = None
    _gene_label: str = None

@dataclass
class MmeResponse:
    disclaimer: str = None
    terms: str = "https://monarchinitiative.org/about/disclaimer"
    results: List[Result] = field(default_factory=list)



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
