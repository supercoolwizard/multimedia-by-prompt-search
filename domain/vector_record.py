from dataclasses import dataclass

@dataclass
class VectorRecord:
    id: str
    vector: list
    metadata: dict


