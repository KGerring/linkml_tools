from ontobio.config import get_config

from diskcache import Cache
import tempfile
import requests


cache = Cache(tempfile.gettempdir())


@cache.memoize()
def get_curie_map(url=None):
    """
    Get CURIE prefix map from SciGraph cypher/curies endpoint
    """
    if url is None:
        url = '{}/cypher/curies'.format(get_config().scigraph_data.url)
    response = requests.get(url)
    if response.status_code == 200:
        curie_map = response.json()
    else:
        curie_map = {}

    return curie_map



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
