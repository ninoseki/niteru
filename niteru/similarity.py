from niteru.structural_similarity import structural_similarity
from niteru.style_similarity import style_similarity


def similarity(html1: str, html2: str, k: float = 0.5) -> float:
    return k * structural_similarity(html1, html2) + (1 - k) * style_similarity(
        html1, html2
    )
