def detect_risk(clause_text):
    text = clause_text.lower()

    if "terminate without notice" in text or "sole discretion" in text:
        return "High"

    if "indemnify" in text or "penalty" in text:
        return "Medium"

    if "non-compete" in text:
        return "High"

    return "Low"