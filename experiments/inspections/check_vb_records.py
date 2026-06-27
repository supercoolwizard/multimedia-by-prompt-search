from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient(path="data/qdrant")
info = client.get_collection("multimedia")


points, next_page_offset = client.scroll(
    collection_name="multimedia",
    limit=10,
    with_vectors=True,
    with_payload=True
)

for p in points:
    print("ID:", p.id)
    print("VECTOR (first 10 dims):", p.vector[:10])
    print("PAYLOAD:", p.payload)
    print("-" * 40)


client.close()
