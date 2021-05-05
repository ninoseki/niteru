from niteru.structural_similarity import structural_similarity
from niteru.style_similarity import style_similarity


def similarity(
    html1: str, html2: str, k: float = 0.5, use_quick_ratio: bool = False
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
    return k * structural_similarity(html1, html2) + (1 - k) * style_similarity(
        html1, html2
    )
