from domain.multimedia import Multimedia
from application.services.multimedia_processor import MultimediaProcessorStrategy


class VideoProcessor(MultimediaProcessorStrategy):
    def __init__(self, slicer, describer, encoder, video_to_image_service):
        self.slicer = slicer
        self.describer = describer
        self.encoder = encoder
        self.vtis = video_to_image_service
        self.prompt = "This is a frame of a video, describe it in detail."

    def process(self, video_path, id):
        timestamps = self.slicer.slice(video_path)

        frames = []

        for timestamp in timestamps:
            frame = self.vtis.video_frame_to_array_ffmpeg(video_path, timestamp)

            description = self.describer.describe(frame, self.prompt)
            vector = self.encoder.encode(description)

            metadata = {
                "path": video_path,
                "text_description": description,
                "entity_type": "frame",
                "timestamp": timestamp,
            }

            frame_data = Multimedia(
                id=id,
                vector=vector,
                metadata=metadata,
            )

            frames.append(frame_data)

        return frames

