from rich.progress import Progress
from time import perf_counter

class ProcessDirectoryUseCase:
    def __init__(self, type_finder, dispatcher, target_dir, id_generator):
        self.type_finder = type_finder
        self.dispatcher = dispatcher
        self.target_dir = target_dir
        self.id_generator = id_generator

    def execute(self):
        results = []

        files = list(self.target_dir.iterdir())

        with Progress() as progress:
            task = progress.add_task(
                "[green]Processing files...", total=len(files)
            )

            for file_path in files:
                start = perf_counter()

                file_path = str(file_path)
                current_id = self.id_generator.generate_id(file_path)
                media_type = self.type_finder.find_type(file_path)

                if media_type is None:
                    progress.advance(task)
                    continue

                result = self.dispatcher.dispatch(
                    media_type,
                    file_path,
                    current_id,
                )

                results.extend(result)

                elapsed = perf_counter() - start
                progress.console.print(
                    f"{file_path}: {elapsed:.2f}s"
                )

                progress.advance(task)

        return results
