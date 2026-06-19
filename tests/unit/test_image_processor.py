from unittest.mock import Mock
from application.image_processor import ImageProcessor

def test_process_image_pipeline():
    describer = Mock()
    encoder = Mock()

    describer.describe.return_value = "a cat"
    encoder.encode.return_value = [0.1, 0.2, 0.3]

    processor = ImageProcessor(describer, encoder)

    fake_image = object()
    processor.image_preprocessor = Mock(return_value=fake_image)

    result = processor.process("image.jpg")

    processor.image_preprocessor.assert_called_once_with("image.jpg")
    describer.describe.assert_called_once_with(fake_image)
    encoder.encode.assert_called_once_with("a cat")

    assert result.text_desciription == "a cat"
    assert result.embedding == [0.1, 0.2, 0.3]
    assert result.path == "image.jpg"
