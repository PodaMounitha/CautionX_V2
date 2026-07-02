from typing import Dict


def evaluate_risk(features: Dict, ml_score: float, vt_result: Dict):

    score = 0

    reasons = []

    # -----------------------------------
    # Machine Learning
    # -----------------------------------

    if ml_score >= 95:
        score += 40
        reasons.append("High machine learning confidence")

    elif ml_score >= 80:
        score += 30
        reasons.append("Moderate machine learning confidence")

    elif ml_score >= 60:
        score += 20
        reasons.append("Low machine learning confidence")

    # -----------------------------------
    # Suspicious Keywords
    # -----------------------------------

    if features["keyword_count"] >= 3:
        score += 20
        reasons.append("Multiple suspicious keywords detected")

    elif features["keyword_count"] >= 1:
        score += 10
        reasons.append("Suspicious keyword detected")

    # -----------------------------------
    # Suspicious TLD
    # -----------------------------------

    if features["suspicious_tld"] == 1:
        score += 15
        reasons.append("Suspicious top-level domain")

    # -----------------------------------
    # Hyphens
    # -----------------------------------

    if features["hyphen_count"] >= 2:
        score += 5
        reasons.append("Multiple hyphens detected")

    # -----------------------------------
    # IP Address
    # -----------------------------------

    if features["ip_present"] == 1:
        score += 15
        reasons.append("IP address used instead of domain")

    # -----------------------------------
    # Entropy
    # -----------------------------------

    if features["entropy"] >= 4.5:
        score += 10
        reasons.append("High URL entropy")

    # -----------------------------------
    # VirusTotal
    # -----------------------------------

    if vt_result["engines"] >= 10:
        score += 30
        reasons.append(
            f"Detected by {vt_result['engines']} security engines"
        )

    elif vt_result["engines"] >= 5:
        score += 20
        reasons.append(
            f"Detected by {vt_result['engines']} security engines"
        )

    elif vt_result["engines"] >= 1:
        score += 10
        reasons.append(
            "Detected by VirusTotal"
        )

    # -----------------------------------
    # Safe Domain Heuristic
    # -----------------------------------

    if (
        features["keyword_count"] == 0
        and features["hyphen_count"] == 0
        and features["suspicious_tld"] == 0
        and features["ip_present"] == 0
        and vt_result["engines"] == 0
    ):
        score = min(score, 15)

        reasons = [
            "No suspicious indicators detected"
        ]

    # -----------------------------------
    # Risk Level
    # -----------------------------------

    if score >= 75:

        prediction = "Malicious"

        risk = "HIGH"

        recommendation = "Do not visit this URL."

    elif score >= 50:

        prediction = "Suspicious"

        risk = "MEDIUM"

        recommendation = (
            "Proceed with caution."
        )

    else:

        prediction = "Safe"

        risk = "LOW"

        recommendation = (
            "No major indicators were detected."
        )

    return {

        "prediction": prediction,

        "risk_level": risk,

        "risk_score": score,

        "recommendation": recommendation,

        "reasons": reasons

    }