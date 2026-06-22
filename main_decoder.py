from application.vector_db_processor import VectorDBProcessor
from infrastructure.multimedia_type_detector import MultimediaTypeFinder

from main_encoder import encoder
from main_encoder import db

from dotenv import load_dotenv
import os

load_dotenv()
hf_token = os.getenv("HF_TOKEN")

mtf = MultimediaTypeFinder()
db_processor = VectorDBProcessor()

prompt = "image of a cat with emoji overlay"
encoded_prompt = encoder.encode(prompt)[0]

results = db.search(encoded_prompt, 1)
print(results)

db.client.close()

# points, next_page_offset = db.client.scroll(
#     collection_name="multimedia",
#     limit=10,
#     with_vectors=True,
#     with_payload=True
# )
#
# for p in points:
#     print("ID:", p.id)
#     print("VECTOR (first 10 dims):", p.vector[:10])
#     print("PAYLOAD:", p.payload)
#     print("-" * 40)
