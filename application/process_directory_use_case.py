class ProcessDirectoryUseCase:
    def __init__(self, mtf, dispatcher, target_dir):
        self.mtf = mtf
        self.dispatcher = dispatcher
        self.target_dir = target_dir

    def execute(self):
        results = []

        for file_path in self.target_dir.iterdir():
            file_path = str(file_path)
            media_type = self.mtf.find_type(file_path)
            result = self.dispatcher.dispatch(media_type, file_path)
            results.append(result)

        return results
