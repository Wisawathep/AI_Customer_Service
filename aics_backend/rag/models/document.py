from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Document:
    content: str
    source: str
    filename: str
    category: str
    metadata: Dict = field(default_factory=dict)