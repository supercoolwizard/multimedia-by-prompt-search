from transformers import AutoTokenizer

class Tokenizer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-large-en-v1.5")

    def tokenize(self, text):
        tokens = self.tokenizer.tokenize(text)
        ids = self.tokenizer.encode(text)

        print(tokens)
        print(ids)
