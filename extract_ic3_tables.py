import tabula
import pandas as pd
from pathlib import Path

PDF = "data/2022_IC3ElderFraudReport.pdf"
OUT = Path("data/clean_tables")
OUT.mkdir(parents=True, exist_ok=True)

PAGES = {
    "age_groups": 5,
    "crime_counts": 6,
    "crime_losses": 7,
    "three_year_counts": 8,
    "three_year_losses": 9,
    "crypto_losses": 16
}

for name, page in PAGES.items():
    print(f"Extracting {name} (page {page})")

    dfs = tabula.read_pdf(
        PDF,
        pages=page,
        lattice=True,
        multiple_tables=True
    )

    combined = pd.concat(dfs)
    combined.to_csv(OUT / f"{name}.csv", index=False)
