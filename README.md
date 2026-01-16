# 🛡️ PhishGuard — Hybrid Phishing Detection System

PhishGuard is a **hybrid phishing detection system** that combines **rule-based cybersecurity logic** with **interpretable machine learning** to accurately detect phishing emails while minimizing false positives.

Unlike black-box models, PhishGuard prioritizes **explainability, severity-aware decisions, and security correctness**, closely mirroring how real-world email security gateways operate.

---

## 🚀 Features

* **Hybrid Detection Engine**

  * Rule-based threat detection for high-severity indicators
  * Machine learning–based NLP classification for language patterns
  * Rule-based logic **overrides ML predictions** when required

* **Explainable AI**

  * Displays *why* an email was flagged
  * Shows ML confidence scores and decision basis

* **Real-World Ready Design**

  * Severity-aware rules (critical, strong, weak
  * Interpretable ML model (TF-IDF + Logistic Regression)
  * Clean separation of training and inference logic

* **Web Interface**

  * Flask-based dashboard for email analysis
  * Clear verdicts: Safe / Suspicious / Phishing

---

## 🧠 Detection Strategy (How It Works)

PhishGuard follows a **layered security approach**:

### 1️⃣ Rule-Based Detection (Security First)

Detects high-risk phishing indicators such as:

* IP-based URLs
* Suspicious top-level domains
* Urgency and threat language
* Social engineering patterns

Certain rules are marked **critical** and immediately elevate risk.

---

### 2️⃣ Machine Learning Detection (Language Intelligence)

* Uses **TF-IDF** to convert email text into numerical features
* Trains a **Logistic Regression** classifier on real phishing datasets
* Outputs a phishing **probability score**

This model is fully interpretable — feature weights can be inspected.

---

### 3️⃣ Hybrid Decision Engine (Final Verdict)

The final decision is made using a **rule-first strategy**:

```
IF critical rule triggered → Phishing
ELSE IF rule = Suspicious AND ML confidence high → Phishing
ELSE IF ML confidence moderate → Suspicious
ELSE → Safe
```

This ensures:

* High recall for real phishing attacks
* Low false positives for legitimate emails
* Explainable and defensible decisions

---

## 🏗️ Architecture Overview

```
User Input
   ↓
Rule-Based Analysis
   ↓
ML Classifier (TF-IDF + Logistic Regression)
   ↓
Hybrid Decision Engine
   ↓
Final Verdict + Explanation
```

---

## 🛠️ Tech Stack

* **Backend:** Flask, Python
* **Machine Learning:** Scikit-learn (TF-IDF, Logistic Regression)
* **NLP:** Text preprocessing, feature weighting
* **Data Processing:** Pandas
* **Model Persistence:** Joblib
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
phishguard/
│
├── app.py                  # Flask application
│
├── detector/
│   ├── rules.py             # URL-based phishing rules
│   ├── text_rules.py        # Email text phishing rules
│   ├── risk_engine.py       # Rule-based risk scoring
│   ├── hybrid_engine.py     # Hybrid ML + rule decision logic
│   └── logger.py            # Detection logging
│
├── scripts/
│   ├── tfidf_prepare.py     # Feature extraction
│   ├── train_model.py       # ML training script
│   └── log_to_csv.py        # Dataset preparation
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── data/
│   └── external_clean.csv   # Clean training dataset
│
├── models/                  # Saved ML artifacts (optional)
│
├── logs/                    # Detection logs
│
└── README.md
```

---

## 📊 Model Performance

* **Accuracy:** ~96%
* **Phishing Recall:** ~96%
* **Precision:** ~94%

The model successfully learns phishing language patterns such as:

* *urgent, verify, click, free, offer*

While recognizing legitimate email patterns such as:

* *meeting, attached, university, thanks*

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/phishguard.git
cd phishguard
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Train the ML model

```bash
python scripts/train_model.py
```

### 5️⃣ Start the Flask app

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 🧪 Example Use Cases

* Detect phishing emails before users click malicious links
* Analyze suspicious emails for security awareness training
* Demonstrate explainable AI in cybersecurity interviews
* Extend detection to SMS, messaging platforms, or browser extensions

---

## 📌 Key Design Principles

* **Explainability over black-box accuracy**
* **Security rules override ML predictions**
* **Precision-first approach to reduce false positives**
* **Modular design for easy extension**

---

## 🔮 Future Enhancements

* User feedback loop for false positives
* Modern phishing fine-tuning with recent datasets
* Dashboard analytics and attack trends
* SMS / WhatsApp phishing detection
* Browser extension integration
* Cloud deployment

