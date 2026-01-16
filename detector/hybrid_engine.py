def hybrid_verdict(rule_verdict, ml_probability):
    """
    rule_verdict: 'Phishing', 'Suspicious', or None
    ml_probability: float between 0 and 1
    """

    # Rule override (absolute authority)
    if rule_verdict == "Phishing":
        return "Phishing", "Rule override"

    if rule_verdict == "Suspicious":
        if ml_probability >= 0.8:
            return "Phishing", "Rule + ML agreement"
        return "Suspicious", "Rule-based suspicion"

    # No strong rules triggered → rely on ML
    if ml_probability >= 0.8:
        return "Phishing", "ML high confidence"
    elif ml_probability >= 0.5:
        return "Suspicious", "ML moderate confidence"
    else:
        return "Safe", "ML low risk"
