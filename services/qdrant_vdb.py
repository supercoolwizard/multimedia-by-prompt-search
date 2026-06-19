from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

class QdrantVectorDatabase:
    def __init__(self):
        self.collection_name = "multimedia"
        self.size = 384
        self.client = QdrantClient(path="data/qdrant")
        self.distance = Distance.COSINE

        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=self.size,
                distance=Distance.COSINE
            )
        )

    def upsert(self, record):
        point = PointStruct(
            id=record.id,
            vector=record.vector,
            payload=record.metadata
        )

        self.client.upsert(
            collection_name=self.collection_name,
            points=[point]
        )

    # def create(self, id, vector, text_description, path, timestamp=None):
    #     self.client.upsert(
    #         collection_name=self.collection_name,
    #         points=[
    #             PointStruct(
    #                 id=id,
    #                 vector=vector,
    #                 payload={
    #                     "text_description": text_description,
    #                     "path": path
    #                     "timestamp": timestamp
    #                 }
    #             )
    #         ]
    #     )

    def search(self, query_vector, limit):
        hits = self.client.query_points(
            collection_name = self.collection_name,
            query = query_vector,
            limit = limit
        )

        return hits



