from niteru.html_parser import NiteruHTMLParser, parse_html

html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- foo -->
  </head>
  <body>
    <p class='foo bar' id='a b c'>foo</p><p class='foo bar'>bar</p>
  </body>
</html>
"""


def test_parser():
    parser = NiteruHTMLParser()
    parser.feed(html)

    assert parser.classes == ["foo", "bar", "foo", "bar"]
    assert parser.tags == [
        "declaration",
        "html",
        "head",
        "meta",
        "meta",
        "meta",
        "title",
        "comment",
        "body",
        "p",
        "p",
    ]


def test_parse_html():
    parsed = parse_html(html)
    assert parsed.classes == ["foo", "bar", "foo", "bar"]
    assert parsed.tags == [
        "declaration",
        "html",
        "head",
        "meta",
        "meta",
        "meta",
        "title",
        "comment",
        "body",
        "p",
        "p",
    ]
