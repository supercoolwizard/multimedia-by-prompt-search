from pathlib import Path
from dotenv import load_dotenv
import os

from settings import TARGET_DIR

from application.services.multimedia_dispatcher import MultimediaDispatcher
from infrastructure.services.video_slicer import VideoSlicer
from infrastructure.bge_small_encoder import BGEEncoder
from infrastructure.fastvlm_image_describer import FastVLMImageDescriber
from infrastructure.qdrant_vdb import QdrantVectorDatabase
from infrastructure.services.multimedia_type_detector import MultimediaTypeFinder
from infrastructure.services.video_to_image_service import VideoToImageService
from application.services.image_processor import ImageProcessor
from application.services.video_processor import VideoProcessor
from application.process_directory_use_case import ProcessDirectoryUseCase
from application.vector_db_processor import VectorDBProcessor

load_dotenv("config.env")
hf_token = os.getenv("HF_TOKEN")

mtf = MultimediaTypeFinder()
describer = FastVLMImageDescriber(hf_token)
encoder = BGEEncoder(hf_token)
slicer = VideoSlicer()
vtis = VideoToImageService()
db_processor = VectorDBProcessor()

db = QdrantVectorDatabase()
db.create_collection()

image_processor = ImageProcessor(describer, encoder)
video_processor = VideoProcessor(slicer, describer, encoder, vtis)

dispatcher = MultimediaDispatcher(image_processor, video_processor)
runner = ProcessDirectoryUseCase(mtf, dispatcher, TARGET_DIR)

filled_entities = runner.execute()

for entity in filled_entities:
    record = db_processor.to_record(entity)
    db.upsert(record)


