from dataclasses import dataclass
from typing import List


@dataclass
class ParsedHTML:
    html: str
    tags: List[str]
    classes: List[str]
