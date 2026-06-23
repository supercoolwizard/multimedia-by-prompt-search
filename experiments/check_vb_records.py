from main_encoder import db

points, next_page_offset = db.client.scroll(
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


db.client.close()
