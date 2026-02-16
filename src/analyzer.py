import csv
import json
from pathlib import Path
from typing import List, Dict


def read_csv(file_path: Path) -> List[Dict[str, str]]:
    """
    Read a CSV file and return rows as dictionaries.
    Skips empty rows.
    """
    rows = []
    with file_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if any(row.values()):
                rows.append(row)
    return rows


def summarize(rows: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Generate basic summary statistics.
    """
    return {
        "total_rows": len(rows),
        "non_empty_rows": sum(1 for r in rows if all(v.strip() for v in r.values()))
    }


def write_json(data: Dict, output_path: Path) -> None:
    """
    Write dictionary data to a JSON file.
    """
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def analyze(input_csv: Path, output_json: Path) -> None:
    rows = read_csv(input_csv)
    summary = summarize(rows)
    write_json(summary, output_json)
