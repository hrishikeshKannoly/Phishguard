from flask import Flask, render_template, request

from detector.rules import analyze_url 
from detector.text_rules import analyze_text
from detector.risk_engine import evaluate_risk
from detector.logger import log_detection


import joblib

model = joblib.load("models/phishing_model.pkl")
vectorizer = joblib.load("models/tfidf.pkl")

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    url = request.form.get("url", "")
    text = request.form.get("text", "")

    url_result = analyze_url(url)
    text_result = analyze_text(text)

    result = evaluate_risk(url_result, text_result)
    log_detection(
        {"url": url, "text": text},
        url_result,
        text_result,
        result
    )

    return render_template(
        "result.html", 
        url_result = url_result,
        text_result = text_result,
        result = result,
        explanations = result['explanations']
    )

if __name__ == "__main__":
    app.run()

