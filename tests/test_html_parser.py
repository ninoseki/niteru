from niteru.html_parser import NiteruHTMLParser, parse_html

html = "<p class='foo bar' id='a b c'>foo</p><p class='foo bar'>bar</p>"


def test_parser():
    parser = NiteruHTMLParser()
    parser.feed(html)

    assert parser.classes == ["foo", "bar", "foo", "bar"]
    assert parser.tags == ["p", "p"]


def test_parse_html():
    parsed = parse_html(html)
    assert parsed.classes == ["foo", "bar", "foo", "bar"]
    assert parsed.tags == ["p", "p"]
