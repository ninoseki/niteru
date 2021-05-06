"""
.. include:: ../README.md
"""
import poetry_version

from niteru.similarity import similarity
from niteru.structural_similarity import structural_similarity
from niteru.style_similarity import style_similarity

__version__ = str(poetry_version.extract(source_file=__file__))


__all__ = ["structural_similarity", "style_similarity", "similarity"]
