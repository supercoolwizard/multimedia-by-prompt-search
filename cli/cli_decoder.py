from rich.console import Console
import argparse

class CLIDecoder:
    def __init__(self, 
                 SEARCH_SCOPE,
                 encoder, 
                 db, 
                 mtf, 
                 output_processor, 
                 table_maker,
                 revealer,
                 ):
        self.SEARCH_SCOPE = SEARCH_SCOPE 
        self.encoder = encoder
        self.db = db
        self.mtf = mtf
        self.output_processor = output_processor
        self.table_maker = table_maker
        self.revealer = revealer
        self.console = Console()

    def _prompt_finder(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("prompt", nargs="?", help="Search prompt")

        args = parser.parse_args()

        prompt = args.prompt or input("Prompt: ")

        return prompt,

    def execute(self):
        prompt = self._prompt_finder()
        embedding = self.encoder.encode(prompt)
        results = self.db.search(embedding, self.SEARCH_SCOPE)

        rows = self.output_processor.create_dict_of_rows(results)

        self.console.print(self.table_maker.make_table(rows))

        idx = int(input("Select index: "))
        self.revealer.reveal_file(rows[idx]["path"])

        self.db.client.close()


