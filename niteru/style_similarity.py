from typing import List

from niteru.html_parser import parse_html
from niteru.utils import is_html


def jaccard_similarity(classes1: List[str], classes2: List[str]) -> float:
    set1 = set(classes1)
    set2 = set(classes2)
    intersection = len(set1 & set2)

    if len(set1) == 0 and len(set2) == 0:
        return 1.0

    denominator = len(set1) + len(set2) - intersection
    return intersection / max(denominator, 0.000001)


def style_similarity_by_classes(classes1: List[str], classes2: List[str]) -> float:
    """Computes CSS style similarity between two DOM trees

    Args:
        classes1 (List[str]): HTML DOM classes
        classes2 (List[str]): HTML DOM classes

    Returns:
        float: Similarity as a float in the range 0.0 to 1.0.
    """
    return jaccard_similarity(classes1, classes2)


def style_similarity(html1: str, html2: str) -> float:
    """Computes CSS style similarity between two DOM trees from HTMLs

    Args:
        html1 (str): HTML string
        html2 (str): HTML string

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

    return style_similarity_by_classes(parsed1.classes, parsed2.classes)
