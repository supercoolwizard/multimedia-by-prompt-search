from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

global_limit = 100

client = QdrantClient(path="data/qdrant")
info = client.get_collection("multimedia")


points, next_page_offset = client.scroll(
    collection_name="multimedia",
    limit=global_limit,
    with_vectors=True,
    with_payload=True
)

for p in points:
    print("ID:", p.id)
    print("VECTOR (first 10 dims):", p.vector[:10])
    print("PAYLOAD:", p.payload)
    print("-" * 40)


client.close()

print(len(points))
