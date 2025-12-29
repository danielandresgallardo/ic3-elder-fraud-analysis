import pdfplumber
import json
from pathlib import Path

PDF_PATH = "data/2022_IC3ElderFraudReport.pdf"
OUTPUT_FILE = Path("data/ic3_text.json")
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

def extract_text():
    pages = []

    with pdfplumber.open(PDF_PATH) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            pages.append({
                "page": i + 1,
                "text": text
            })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(pages, f, indent=2, ensure_ascii=False)

    print("Text saved to data/ic3_text.json")

if __name__ == "__main__":
    extract_text()
