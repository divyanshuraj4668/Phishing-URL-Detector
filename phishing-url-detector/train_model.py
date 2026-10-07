from pathlib import Path
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from model.features import extract_features

MODEL_PATH = Path("model/phishing_model.joblib")
DATA_PATH = Path("data/demo_urls.csv")

def train_model():
    df = pd.read_csv(DATA_PATH)

    feature_names = [
        "url_length", "hostname_length", "path_length", "dot_count",
        "hyphen_count", "at_count", "question_count", "equal_count",
        "slash_count", "digit_count", "subdomain_count",
        "has_https", "has_ip_address", "has_suspicious_word"
    ]

    X = pd.DataFrame([extract_features(url) for url in df["url"]])[feature_names]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=120,
        max_depth=8,
        random_state=42
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print("Demo dataset accuracy:", round(accuracy_score(y_test, predictions), 3))
    print(classification_report(y_test, predictions, zero_division=0))

    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
