from rich.table import Table


class TableMaker:
    def make_table(self, dictionary_of_rows):
        table = Table(show_lines=True)
        table.add_column("Index")
        table.add_column("Best Match Path")
        table.add_column("Score")
        table.add_column("Description")

        for index, row in enumerate(dictionary_of_rows):
            table.add_row(
                str(index),
                row["path"], 
                row["score"],
                row["text_description"],
            )

        return table
