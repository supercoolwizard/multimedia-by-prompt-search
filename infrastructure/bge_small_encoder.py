from application.ports.text_encoder import TextEncoder
from transformers import AutoTokenizer, AutoModel
import torch

class BGEEncoder(TextEncoder):
    def __init__(self, hf_token):
        self.model_name = "BAAI/bge-small-en-v1.5"
        self.model = AutoModel.from_pretrained(self.model_name, token=hf_token)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, token=hf_token)

    def encode(self, text):
        self.model.eval()
        encoded_input = self.tokenizer(text, padding=True, truncation=True, return_tensors='pt')

        with torch.no_grad():
            model_output = self.model(**encoded_input)
            sentence_embeddings = model_output[0][:, 0]

        sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
        return sentence_embeddings.tolist()
