from niteru.similarity import similarity

html1 = """
<html>
<h1 class="title">First Document</h1>
<ul class="menu">
    <li class="active">Documents</li>
    <li>Extra</li>
</ul>
</html>
"""

html2 = """
<html>
<h1 class="title">Second document Document</h1>
<ul class="menu">
    <li class="active">Extra Documents</li>
</ul>
</html>
"""


def test_similarity():
    assert similarity(html1, html2) > 0.90


def test_similarity_with_invalid_inputs():
    assert similarity("a", "b") == 0.0
    assert similarity("<p>foo</p>", "b") == 0.0
    assert similarity("a", "<p>bar</p>") == 0.0
