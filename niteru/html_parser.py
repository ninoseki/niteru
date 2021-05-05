from functools import lru_cache
from html.parser import HTMLParser
from typing import List, Optional, Tuple, cast

from niteru.dataclasses import ParsedHTML


class NiteruHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()

        self.tags: List[str] = []
        self.classes: List[str] = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        self.tags.append(tag)

        for attr in attrs:
            key, value = attr
            if key == "class" and value is not None:
                self.classes.extend(value.split())

    def handle_comment(self, _: str) -> None:
        self.tags.append("comment")

    def handle_decl(self, decl: str) -> None:
        self.tags.append("declaration")


@lru_cache(maxsize=128)
def _parse_html(html: str):
    parser = NiteruHTMLParser()
    parser.feed(html)

    return ParsedHTML(html=html, tags=parser.tags, classes=parser.classes)


def parse_html(html: str) -> ParsedHTML:
    parsed = _parse_html(html)
    return cast(ParsedHTML, parsed)
