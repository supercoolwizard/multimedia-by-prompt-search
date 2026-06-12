
class ImageProcessor:
    def __init__(self, type_detector, describer, tokenizer):
        self.type_detector = type_detector
        self.describer = describer
        self.tokenizer = tokenizer

    def process(self, image, multimedia):
        multimedia.type = self.type_detector
        multimedia.description = self.describer.describe(image)
        multimedia.embeddings = self.tokenizer.tokenize(multimedia.description)

        return multimedia
