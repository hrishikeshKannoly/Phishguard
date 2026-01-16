import json
import csv

INPUT_LOG = "logs/detections.log"
OUTPUT_CSV = "data/training_data.csv"

rows = []

with open(INPUT_LOG, "r") as f:
    for line in f:
        entry = json.loads(line)
        verdict = entry["final_result"]["verdict"]

        if verdict not in ["Safe", "Phishing"]:
            continue  # skip Suspicious for now

        rows.append({
            "text": entry["input"].get("text", ""),
            "url": entry["input"].get("url", ""),
            "label": 1 if verdict == "Phishing" else 0
        })

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["text", "url", "label"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Saved {len(rows)} rows to {OUTPUT_CSV}")
