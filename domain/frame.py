from dataclasses import dataclass
from domain.multimedia import Multimedia

@dataclass
class Frame(Multimedia):
    timestamp: float

    # def to_dict(self):
    #     return {
    #         "vector": self.embedding,
    #         "metadata": {
    #             "text_description": self.text_description,
    #             "timestamp": self.timestamp,
    #             "path": self.path
    #         }
    #     }
