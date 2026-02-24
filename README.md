# CSV Log Analyzer

A lightweight Python utility to analyze CSV/log-style data and generate summary statistics.

## Features
- Reads CSV files safely
- Skips empty rows
- Generates summary statistics
- Exports results as formatted JSON
- Includes pytest-based test coverage

## Project Structure

csv_log_analyzer/
├── src/
│   └── analyzer.py
├── tests/
│   └── test_analyzer.py
├── data/
└── README.md

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/csv-log-analyzer.git
cd csv-log-analyzer
python -m venv venv
venv\Scripts\activate
pip install pytest
