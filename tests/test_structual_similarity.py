from niteru.structural_similarity import structural_similarity

html1 = """
<h1 class="title">First Document</h1>
<ul class="menu">
    <li class="active">Documents</li>
    <li>Extra</li>
</ul>
"""

html2 = """
<h1 class="title">Second document Document</h1>
<ul class="menu">
    <li class="active">Extra Documents</li>
</ul>
"""


def test_structural_similarity():
    assert structural_similarity(html1, html2) > 0.85
    assert structural_similarity(html1, html2, use_quick_ratio=True) > 0.85
