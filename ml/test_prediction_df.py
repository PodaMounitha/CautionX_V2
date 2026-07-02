import pandas as pd
import joblib
from feature_extraction import extract_features

model = joblib.load("url_model.pkl")

urls = [
    "google.com",
    "github.com",
    "openai.com",
    "paypal-login-security.net",
    "amazon-update-account.tk"
]

for url in urls:

    X = pd.DataFrame([extract_features(url)])

    pred = model.predict(X)[0]

    probs = model.predict_proba(X)[0]

    print("\nURL:", url)
    print("Prediction:", pred)
    print("Probabilities:", probs)