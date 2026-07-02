from flask import Flask, request, jsonify
from flask_cors import CORS

import pandas as pd
import joblib

from feature_extraction import extract_features
from virustotal_service import check_virustotal
from decision_engine import evaluate_risk

app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("url_model.pkl")


@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "service": "Caution-X V2 Backend"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Invalid JSON request"
            }), 400

        url = data.get("url", "").strip()

        if url == "":
            return jsonify({
                "error": "URL is required"
            }), 400

        # -----------------------------
        # Feature Extraction
        # -----------------------------
        features = extract_features(url)

        X = pd.DataFrame([features])

        # -----------------------------
        # ML Prediction
        # -----------------------------
        prediction = model.predict(X)[0]

        probabilities = model.predict_proba(X)[0]

        ml_confidence = float(max(probabilities) * 100)

        # -----------------------------
        # Decide whether VirusTotal is needed
        # -----------------------------

        suspicious_features = (

            features["keyword_count"] > 0
            or features["suspicious_tld"] == 1
            or features["hyphen_count"] >= 2
            or features["ip_present"] == 1
            or features["entropy"] > 4.5

        )

        vt_checked = False

        vt_result = check_virustotal(url)
        vt_checked = True

        # -----------------------------
        # Decision Engine
        # -----------------------------

        result = evaluate_risk(
            features,
            ml_confidence,
            vt_result
        )

        # -----------------------------
        # Final Response
        # -----------------------------

        response = {

            "url": url,

            "prediction": result["prediction"],

            "risk_level": result["risk_level"],

            "risk_score": result["risk_score"],

            "confidence": round(ml_confidence, 2),

            "ml_prediction": (
                "Malicious"
                if prediction == 1
                else "Safe"
            ),

            "virustotal_checked": vt_checked,

            "virustotal": {

                "status": vt_result["status"],

                "engines_detected": vt_result["engines"],

                "malicious": vt_result["malicious"],

                "suspicious": vt_result["suspicious"],

                "harmless": vt_result["harmless"],

                "score": vt_result["score"]

            },

            "reasons": result["reasons"],

            "recommendation": result["recommendation"]

        }

        return jsonify(response)

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500


if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )