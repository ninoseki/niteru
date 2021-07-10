from difflib import SequenceMatcher
from typing import List

from niteru.html_parser import parse_html
from niteru.utils import is_html


def structural_similarity_by_tags(
    tags1: List[str], tags2: List[str], *, use_quick_ratio: bool = False
) -> float:
    """Computes the structural similarity between two DOM trees

    Args:
        tags1 (List[str]): HTML DOM tags
        tags2 (List[str]): HTML DOM tags
        use_quick_ratio (bool, optional): Whether to use difflib.SequenceMatcher.quick_ratio function for computing similarity or not. Use difflib.SequenceMatcher.ratio function by default. Defaults to False.

    Returns:
        float: Similarity as a float in the range 0.0 to 1.0.
    """
    diff: SequenceMatcher = SequenceMatcher()
    diff.set_seq1(tags1)
    diff.set_seq2(tags2)

    if use_quick_ratio:
        return diff.quick_ratio()

    return diff.ratio()


def structural_similarity(
    html1: str, html2: str, *, use_quick_ratio: bool = False
) -> float:
    """Computes the structural similarity between two DOM trees from HTMLs

    Args:
        html1 (str): HTML string
        html2 (str): HTML string
        use_quick_ratio (bool, optional): Whether to use difflib.SequenceMatcher.quick_ratio function for computing similarity or not. Use difflib.SequenceMatcher.ratio function by default. Defaults to False.

    Returns:
        float: Similarity as a float in the range 0.0 to 1.0.
    """
    try:
        parsed1 = parse_html(html1)
        parsed2 = parse_html(html2)
    except Exception:
        return 0.0

    # returns 0.0 if there is a non-html input
    if not is_html(parsed1) or not is_html(parsed2):
        return 0.0

    return structural_similarity_by_tags(
        parsed1.tags, parsed2.tags, use_quick_ratio=use_quick_ratio
    )
