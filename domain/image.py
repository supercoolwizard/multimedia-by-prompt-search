from dataclasses import dataclass
from multimedia import Multimedia

@dataclass
class Image(Multimedia):
    text_desciription: str
    embedding: list
    path: str
