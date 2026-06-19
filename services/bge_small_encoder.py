from infrastructure.text_encoder import TextEncoder
from sentence_transformers import SentenceTransformer

class BGEEncoder(TextEncoder):
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")
        self.tokenizer = self.model._first_module().tokenizer

    def encode(self, text):
        embedding = self.model.encode(text)
        return embedding.tolist()
