from unittest.mock import Mock
from application.image_processor import ImageProcessor

def test_process_image_calls_dependencies_in_order():
    describer = Mock()
    tokenizer = Mock()
    encoder = Mock()

    describer.describe.return_value = "a terrified cat with a terrified emoji over it"
    tokenizer.tokenize.return_value = ["a", "terrified", "cat", "with", "a", "terrified", "emoji", "over", "it"]
    encoder.encode.return_value = [0.123, -0.123, 0.001]

    processor = ImageProcessor(describer, tokenizer, encoder)

    image_data = processor.process("image.jpg")

    assert image_data.text_desciription == "a terrified cat with a terrified emoji over it"
    assert image_data.embedding == [0.123, -0.123, 0.001]
    assert image_data.path == "image.jpg"

