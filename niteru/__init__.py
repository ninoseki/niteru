"""
.. include:: ../README.md
"""
from niteru.similarity import similarity
from niteru.structural_similarity import structural_similarity
from niteru.style_similarity import style_similarity

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

__version__ = importlib_metadata.version(__name__)


__all__ = ["structural_similarity", "style_similarity", "similarity"]
