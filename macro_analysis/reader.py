import csv
from pathlib import Path

def read_csv(file_path):
    all_data = []
    for file in file_path:
        path = Path(file)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        with open(path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            all_data.extend(reader)
    return all_data
