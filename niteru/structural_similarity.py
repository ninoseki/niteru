from difflib import SequenceMatcher

from niteru.html_parser import parse_html
from niteru.utils import is_html


def structural_similarity(
    html1: str, html2: str, use_quick_ratio: bool = False
) -> float:
    """Computes the structural similarity between two DOM trees

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

    tags1 = parsed1.tags
    tags2 = parsed2.tags
    diff: SequenceMatcher = SequenceMatcher()
    diff.set_seq1(tags1)
    diff.set_seq2(tags2)

    if use_quick_ratio:
        return diff.quick_ratio()

    return diff.ratio()
