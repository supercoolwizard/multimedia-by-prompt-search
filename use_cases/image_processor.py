from domain.image import Image

class ImageProcessor:
    def __init__(self, describer, tokenizer):
        self.describer = describer
        self.tokenizer = tokenizer

    def image_preprocessor(self, image_path):
        pass

    def process(self, image_path):
        image = self.image_preprocessor(image_path)
        description = self.describer.describe(image)
        embeddings = self.tokenizer.tokenize(description)
        image_data = Image(
            text_desciription=description,
            embedding=embeddings,
            path=image_path,
        )

        return image_data
