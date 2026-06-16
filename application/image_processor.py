from domain.image import Image
from application.multimedia_processor import MultimediaProcessorStrategy

class ImageProcessor(MultimediaProcessorStrategy):
    def __init__(self, describer, tokenizer, encoder):
        self.describer = describer
        self.tokenizer = tokenizer
        self.encoder = encoder

    def image_preprocessor(self, image_path):
        return image_path

    def process(self, image_path):
        image = self.image_preprocessor(image_path)
        description = self.describer.describe(image)
        tokens = self.tokenizer.tokenize(description)
        embeddings = self.encoder.encode(tokens)

        image_data = Image(
            text_desciription=description,
            embedding=embeddings,
            path=image_path,
        )

        return image_data
