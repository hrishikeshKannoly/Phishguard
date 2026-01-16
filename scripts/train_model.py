import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


df = pd.read_csv("data/external_clean.csv", dtype=str)
# Load dataset
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

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

feature_names = vectorizer.get_feature_names_out()
coefficients = model.coef_[0]

# Top phishing-indicative words
top_phishing = sorted(
    zip(coefficients, feature_names),
    reverse=True
)[:20]

# Top safe-indicative words
top_safe = sorted(
    zip(coefficients, feature_names)
)[:20]

print("\nTop phishing words:")
for coef, word in top_phishing:
    print(word, round(coef, 3))

print("\nTop safe words:")
for coef, word in top_safe:
    print(word, round(coef, 3))

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/phishing_model.pkl")
joblib.dump(vectorizer, "models/tfidf.pkl")