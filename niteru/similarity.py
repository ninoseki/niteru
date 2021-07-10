from typing import List, Tuple

from niteru.html_parser import parse_html
from niteru.structural_similarity import structural_similarity_by_tags
from niteru.style_similarity import style_similarity_by_classes
from niteru.utils import is_html


def similarity_by_tags_and_classes(
    tags: Tuple[List[str], List[str]],
    classes: Tuple[List[str], List[str]],
    *,
    k: float = 0.5,
    use_quick_ratio: bool = False
) -> float:
    """Computes the joint similarity between two DOM trees

    Args:
        tags (Tuple[List[str], List[str]]): HTML DOM tags
        classes (Tuple[List[str], List[str]]): HTML DOM classes
        k (float, optional): Weight of structural_similarity function as a float in the range 0.0 to 1.0. Defaults to 0.5.
        use_quick_ratio (bool, optional): Whether to use difflib.SequenceMatcher.quick_ratio function for computing similarity in structural_similarity function or not. Use difflib.SequenceMatcher.ratio function by default. Defaults to False.

    Returns:
        float: Similarity as a float in the range 0.0 to 1.0.
    """
    tags1, tags2 = tags
    structural_similarity = structural_similarity_by_tags(
        tags1, tags2, use_quick_ratio=use_quick_ratio
    )

    classes1, classes2 = classes
    style_similarity = style_similarity_by_classes(classes1, classes2)

    return k * structural_similarity + (1 - k) * style_similarity


def similarity(
    html1: str, html2: str, *, k: float = 0.5, use_quick_ratio: bool = False
) -> float:
    """Computes the joint similarity between two DOM trees

    Args:
        html1 (str): HTML string
        html2 (str): HTML string
        k (float, optional): Weight of structural_similarity function as a float in the range 0.0 to 1.0. Defaults to 0.5.
        use_quick_ratio (bool, optional): Whether to use difflib.SequenceMatcher.quick_ratio function for computing similarity in structural_similarity function or not. Use difflib.SequenceMatcher.ratio function by default. Defaults to False.

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

    tags = (parsed1.tags, parsed2.tags)
    classes = (parsed1.classes, parsed2.classes)
    return similarity_by_tags_and_classes(
        tags, classes, k=k, use_quick_ratio=use_quick_ratio
    )
