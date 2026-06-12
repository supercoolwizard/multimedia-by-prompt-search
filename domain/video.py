from dataclasses import dataclass
from multimedia import Multimedia

@dataclass
class Video:
    text_desciription: str
    embedding: list
    path: str
    timestamp: float
