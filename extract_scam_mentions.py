import json
import re
import pandas as pd

with open("data/ic3_text.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

SCAM_TYPES = [
    "tech support",
    "romance",
    "investment",
    "phishing",
    "business email compromise",
    "government impersonation",
    "cryptocurrency",
    "lottery",
    "sweepstakes"
]

records = []

for page in pages:
    text = page["text"].lower() if page["text"] else ""
    for scam in SCAM_TYPES:
        if scam in text:
            records.append({
                "page": page["page"],
                "scam_type": scam
            })

df = pd.DataFrame(records)
df.to_csv("data/scam_mentions.csv", index=False)

print("Scam mentions extracted.")

