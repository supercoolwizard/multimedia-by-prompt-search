from pathlib import Path
from application.multimedia_dispatcher import MultimediaDispatcher
from application.vector_db_processor import VectorDBProcessor
from infrastructure.video_slicer import VideoSlicer
from services.bge_small_encoder import BGEEncoder
from services.fastvlm_image_describer import FastVLMImageDescriber
from services.qdrant_vdb import QdrantVectorDatabase
from settings import TARGET_DIR
from infrastructure.multimedia_type_detector import MultimediaTypeFinder
from infrastructure.video_to_image_by_timestamp import VideoToImageService
from application.image_processor import ImageProcessor
from application.video_processor import VideoProcessor
from application.process_directory_use_case import ProcessDirectoryUseCase
from dotenv import load_dotenv
import os

load_dotenv()
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
video_processor = VideoProcessor(slicer, describer, vtis)

dispatcher = MultimediaDispatcher(image_processor, video_processor)
runner = ProcessDirectoryUseCase(mtf, dispatcher, TARGET_DIR)

filled_entities = runner.execute()

for entity in filled_entities:
    record = db_processor.to_record(entity)
    db.upsert(record)


