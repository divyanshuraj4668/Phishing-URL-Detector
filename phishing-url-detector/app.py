from flask import Flask, render_template, request
from model.features import extract_features
import joblib
from pathlib import Path

app = Flask(__name__)

MODEL_PATH = Path("model/phishing_model.joblib")

# Train the bundled model automatically if it does not exist.
if not MODEL_PATH.exists():
    from train_model import train_model
    train_model()

model = joblib.load(MODEL_PATH)

FEATURE_NAMES = [
    "url_length", "hostname_length", "path_length", "dot_count",
    "hyphen_count", "at_count", "question_count", "equal_count",
    "slash_count", "digit_count", "subdomain_count",
    "has_https", "has_ip_address", "has_suspicious_word"
]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    url = ""

    if request.method == "POST":
        url = request.form.get("url", "").strip()

        if url:
            features = extract_features(url)
            X = [[features[name] for name in FEATURE_NAMES]]
            prediction = int(model.predict(X)[0])
            probability = float(max(model.predict_proba(X)[0]))

            result = {
                "label": "Phishing / Suspicious" if prediction == 1 else "Likely Legitimate",
                "is_phishing": prediction == 1,
                "confidence": round(probability * 100, 1)
            }

    return render_template("index.html", result=result, url=url)

if __name__ == "__main__":
    app.run(debug=True)
