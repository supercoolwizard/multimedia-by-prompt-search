from dataclasses import dataclass
from domain.multimedia import Multimedia

@dataclass
class DomainImage(Multimedia):
    pass

    # def to_dict(self):
    #     return {
    #         "vector": self.embedding,
    #         "metadata": {
    #             "text_description": self.text_description,
    #             "path": self.path
    #         }
    #     }


