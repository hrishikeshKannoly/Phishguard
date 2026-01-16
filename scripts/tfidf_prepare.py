import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("data/external_clean.csv", dtype=str)

# report and fix missing text
missing_text = df["text"].isna().sum()
print(f"Missing text rows: {missing_text}")
df["text"] = df["text"].fillna("").astype(str)

# ensure labels are present and numeric
if "label" in df.columns:
    df["label"] = pd.to_numeric(df["label"], errors="coerce")
    missing_labels = df["label"].isna().sum()
    print(f"Missing/invalid labels: {missing_labels}")
    # optionally drop rows with no label
    df = df.dropna(subset=["label"])
else:
    raise SystemExit("ERROR: 'label' column not found in CSV")

X_text = df["text"]
y = df["label"].astype(int)

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=3000,
    token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z]+\b"
)


X = vectorizer.fit_transform(X_text)

print("Feature matrix shape:", X.shape)
print("Number of labels:", y.value_counts())
print("Sample features:", vectorizer.get_feature_names_out()[:20])
