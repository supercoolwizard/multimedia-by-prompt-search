class ProcessDirectoryUseCase:
    def __init__(self, type_finder, dispatcher, target_dir, id_generator):
        self.type_finder = type_finder
        self.dispatcher = dispatcher
        self.target_dir = target_dir
        self.id_generator = id_generator

    def execute(self):
        results = []

        for file_path in self.target_dir.iterdir():
            file_path = str(file_path)
            current_id = self.id_generator.generate_id(file_path)
            media_type = self.type_finder.find_type(file_path)
            result = self.dispatcher.dispatch(media_type, file_path, current_id)
            results.extend(result)

        return results
