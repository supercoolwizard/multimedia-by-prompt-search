from application.vector_db_processor import VectorDBProcessor
from infrastructure.services.multimedia_type_detector import MultimediaTypeFinder

from main_encoder import encoder
from main_encoder import db

from dotenv import load_dotenv
import os

load_dotenv("config.env")
hf_token = os.getenv("HF_TOKEN")

mtf = MultimediaTypeFinder()
db_processor = VectorDBProcessor()

prompt = "image of a cat with emoji overlay"
encoded_prompt = encoder.encode(prompt)[0]

results = db.search(encoded_prompt, 1)
print(results)

db.client.close()


