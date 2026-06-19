from uuid import uuid5, NAMESPACE_URL
from domain.vector_record import VectorRecord

class VectorDBProcessor:
    def generate_id(self, entity):
        if hasattr(entity, "timestamp"):
            key = f"{entity.path}:{entity.timestamp}"
        else:
            key = entity.path

        return str(uuid5(NAMESPACE_URL, key))

    def to_record(self, entity):
        metadata = {
            "path": entity.path,
            "text_description": entity.text_description,
            "entity_type": entity.__class__.__name__
        }

        if hasattr(entity, "timestamp"):
            metadata["timestamp"] = entity.timestamp

        return VectorRecord(
            id=self.generate_id(entity),
            vector=entity.vector,
            metadata=metadata
        )

