from application.ports.output_processor import OutputProcessor


class QdrantOutputProcessor(OutputProcessor):
    def create_dict_of_rows(self, results):
        rows = []

        for result in results.points:
            rows.append({
                "path": result.payload["path"],
                "score": str(result.score),
                "text_description": result.payload["text_description"],
            })

        return rows

    def list_of_paths_maker(self, rows):
        return [row["path"] for row in rows]
