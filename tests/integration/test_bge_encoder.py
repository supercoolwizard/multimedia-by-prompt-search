from services.bge_small_encoder import BGEEncoder


encoder = BGEEncoder()
embedding = encoder.encode("green cat")
print(embedding)
