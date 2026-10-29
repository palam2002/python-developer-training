
import json
from pathlib import Path


class JsonStorage:
    def __init__(self, folder="data"):
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=True)

    def load(self, filename):
        filepath = self.folder / filename

        if not filepath.exists():
            filepath.write_text("[]", encoding="utf-8")
            return []

        try:
            content = filepath.read_text(encoding="utf-8").strip()

            if not content:
                return []

            records = json.loads(content)

            if not isinstance(records, list):
                raise ValueError("JSON data must be a list.")

            return records

        except (json.JSONDecodeError, ValueError) as error:
            raise RuntimeError(
                f"Cannot read {filepath}: {error}. "
                "Check the JSON file format."
            ) from error

    def save(self, filename, records):
        filepath = self.folder / filename

        with filepath.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)
