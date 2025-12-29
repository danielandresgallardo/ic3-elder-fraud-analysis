import camelot
import pandas as pd
from pathlib import Path

PDF_PATH = "data/2022_IC3ElderFraudReport.pdf"
OUTPUT_DIR = Path("data/tables")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def extract_tables():
    print("Extracting tables...")

    tables = camelot.read_pdf(PDF_PATH, pages="all", flavor="stream")

    print(f"Found {len(tables)} tables")

    for i, table in enumerate(tables):
        df = table.df
        df.to_csv(OUTPUT_DIR / f"table_{i+1}.csv", index=False)

    print("Tables saved to data/tables/")

if __name__ == "__main__":
    extract_tables()
