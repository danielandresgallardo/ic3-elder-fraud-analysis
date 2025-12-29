import pandas as pd
from pathlib import Path

TABLE_DIR = Path("data/tables")
OUTPUT = Path("data/cleaned")

OUTPUT.mkdir(parents=True, exist_ok=True)

def clean_money(x):
    if pd.isna(x):
        return None
    return float(str(x).replace("$","").replace(",","").replace(" ",""))

def normalize():
    all_tables = []

    for file in TABLE_DIR.glob("*.csv"):
        df = pd.read_csv(file)
        df["source"] = file.name
        all_tables.append(df)

    merged = pd.concat(all_tables, ignore_index=True)
    merged.to_csv(OUTPUT / "raw_merged.csv", index=False)

    print("Merged tables saved.")

if __name__ == "__main__":
    normalize()
