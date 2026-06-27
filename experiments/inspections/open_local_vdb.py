from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient(path="data/qdrant")

print(client.get_collections())

info = client.get_collection("multimedia")
print(info)

count = client.count(
    collection_name="multimedia",
    exact=True
)
print("points:", count.count)
