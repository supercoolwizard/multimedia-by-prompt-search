from dataclasses import dataclass
from domain.multimedia import Multimedia

@dataclass
class Frame(Multimedia):
    timestamp: float
