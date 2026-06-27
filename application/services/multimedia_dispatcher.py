class MultimediaDispatcher:
    def __init__(self, image_processor, video_processor):
        self._strategies = {
            "image": image_processor,
            "video": video_processor,
        }

    def dispatch(self, media_type, path, id):
        use_case = self._strategies.get(media_type)
        return use_case.process(path, id)
