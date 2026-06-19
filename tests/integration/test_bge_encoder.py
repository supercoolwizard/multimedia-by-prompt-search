import torch
from services.bge_small_encoder import BGEEncoder

def cosine_similarity(a, b):
    return torch.nn.functional.cosine_similarity(a, b).item()

def test_similar_sentences_are_closer():
    encoder = BGEEncoder()

    cat1 = encoder.encode("green cat")
    cat2 = encoder.encode("cat that is green")
    dog = encoder.encode("airplane engine")

    assert cosine_similarity(cat1, cat2) > cosine_similarity(cat1, dog)
