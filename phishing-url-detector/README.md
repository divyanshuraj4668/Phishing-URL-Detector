# Phishing URL Detection System

A small machine-learning web application that classifies URLs as **likely legitimate** or **suspicious** using URL-based features.

> **Educational project:** The bundled dataset is synthetic and intentionally small. This project demonstrates the ML workflow and should not be used as a real-world security product.

## Features

- URL feature extraction
- Random Forest classification
- Flask web interface
- Confidence score
- Local model persistence with Joblib
- No external API required

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Flask
- HTML/CSS
- Joblib

## How It Works

1. A user enters a URL.
2. The application extracts simple characteristics such as URL length, number of dots, subdomains, HTTPS usage, IP-address usage and suspicious keywords.
3. A Random Forest classifier processes these features.
4. The application displays the predicted class.

## Project Structure

```text
phishing-url-detector/
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── data/
│   └── demo_urls.csv
├── model/
│   ├── __init__.py
│   └── features.py
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Installation

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train_model.py
```

Run the application:

```bash
python app.py
```

Open the local address shown by Flask, normally:

```text
http://127.0.0.1:5000
```

## Example URLs

Try:

```text
https://www.google.com
https://github.com
verify-account-login-security.com
bank-security-verify.com
```

## Future Improvements

- Use a large real-world phishing dataset.
- Add DNS and domain-age information.
- Compare Random Forest with Logistic Regression and XGBoost.
- Add cross-validation and a confusion matrix.
- Deploy the application online.

## Author

**Divyanshu Raj**
