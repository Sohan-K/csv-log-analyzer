from pathlib import Path
from src.analyzer import read_csv, summarize


def test_read_csv():
    sample = Path("data/sample.csv")
    rows = read_csv(sample)
    assert len(rows) == 4


def test_summarize():
    rows = [
        {"a": "1", "b": "2"},
        {"a": "", "b": "3"},
    ]
    summary = summarize(rows)
    assert summary["total_rows"] == 2
    assert summary["non_empty_rows"] == 1
