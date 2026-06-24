from infrastructure.services.multimedia_type_detector import MultimediaTypeFinder

from main_encoder import encoder
from main_encoder import db

from dotenv import load_dotenv
import os

load_dotenv("config.env")
hf_token = os.getenv("HF_TOKEN")

mtf = MultimediaTypeFinder()

prompt = "image of a cat with emoji overlay"
encoded_prompt = encoder.encode(prompt)[0]

results = db.search(encoded_prompt, 1)
print(results)

db.client.close()

# from infrastructure.services.multimedia_type_detector import MultimediaTypeFinder
#
# from infrastructure.bge_small_encoder import BGEEncoder
# from infrastructure.qdrant_vdb import QdrantVectorDatabase
#
# from dotenv import load_dotenv
# import os
#
# load_dotenv("config.env")
# hf_token = os.getenv("HF_TOKEN")
#
# encoder = BGEEncoder(hf_token)
# db = QdrantVectorDatabase()
#
# mtf = MultimediaTypeFinder()
#
# prompt = "image of a cat with emoji overlay"
# encoded_prompt = encoder.encode(prompt)[0]
#
# results = db.search(encoded_prompt, 1)
# print(results)
#
# db.client.close()
#

