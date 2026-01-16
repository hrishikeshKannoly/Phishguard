import pandas as pd

# Load the Excel or CSV file
df = pd.read_csv("data/Phishing_Email.csv")  
# OR if it's Excel:
# df = pd.read_excel("your_file.xlsx")

# Inspect columns (optional but good)
print(df.columns)

# Rename columns to something sane (VERY IMPORTANT)
df = df.rename(columns={
    "Email Text": "text",
    "Email Type": "label"
})

# Map labels to numbers
df["label"] = df["label"].map({
    "Phishing Email": 1,
    "Safe Email": 0
})

# Drop rows where mapping failed (safety)
df = df.dropna(subset=["label"])

# Keep only what we need
df = df[["text", "label"]]

# Save clean version
df.to_csv("data/external_clean.csv", index=False)

print(df.head())
print("Label counts:")
print(df["label"].value_counts())
