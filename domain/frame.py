from dataclasses import dataclass
from multimedia import Multimedia

@dataclass
class Frame:
    text_desciription: str
    embedding: list
    path: str
    timestamp: float
