import json
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient(path="./qdrant")

client.recreate_collection(
    collection_name="docs",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

texts = [
    "Qdrant is a vector database",
    "PostgreSQL is a relational database",
    "Redis is an in-memory datastore"
]

vectors = model.encode(texts).tolist()

client.upsert(
    collection_name="docs",
    points=[
        PointStruct(
            id=i,
            vector=vectors[i],
            payload={"text": texts[i]}
        )
        for i in range(len(texts))
    ]
)

query_vector = model.encode(
    "vector search engine"
).tolist()

hits = client.query_points(
    collection_name="docs",
    query=query_vector,
    limit=3
)

for hit in hits.points:
    print(hit.score, hit.payload["text"])
