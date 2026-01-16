from detector.explanations import RULE_EXPLANATIONS

URL_WEIGHTS = {
    "ip_in_url": 50,
    "suspicious_tld": 25,
    "long_url": 15,
    "uses_https": -5
}

TEXT_WEIGHTS = {
    "threat_detected": 30,
    "urgency_detected": 25,
    "reward_detected": 10
}


CRITICAL_RULES = [
    "ip_in_url",
]

def calculate_url_risk(url_result):
    score = 0
    for rule, triggered in url_result.items():
        if triggered:
            score += URL_WEIGHTS.get(rule, 0)
    return score

def calculate_text_risk(text_result):
    score = 0
    for rule, triggered in text_result.items():
        if triggered:
            score += TEXT_WEIGHTS.get(rule, 0)
    return score

def get_verdict(score):
    if score >= 70:
        return "Phishing"
    elif score >= 40:
        return "Suspicious"
    else:
        return "Safe"
    
def rule_based_verdict(url_result, text_result):
    # Critical override
    if url_result.get("ip_in_url"):
        return "Suspicious"

    # Strong combinations
    strong_hits = 0

    if text_result.get("threat_detected"):
        strong_hits += 1
    if text_result.get("urgency_detected"):
        strong_hits += 1
    if url_result.get("suspicious_tld"):
        strong_hits += 1

    if strong_hits >= 2:
        return "Phishing"

    if strong_hits == 1:
        return "Suspicious"

    return None  # fall back to score


def evaluate_risk(url_analysis, text_analysis):
    total_score = (
        calculate_url_risk(url_analysis) +
        calculate_text_risk(text_analysis)
    )

    triggered_rules = {
        **url_analysis,
        **text_analysis
    }


    if any(triggered_rules.get(rule) for rule in CRITICAL_RULES):
        verdict = "Suspicious"
    else:
        rule_verdict = rule_based_verdict(url_analysis, text_analysis)
        if rule_verdict:
            verdict = rule_verdict
        else:
            verdict = get_verdict(total_score)

    explanations = get_explanations(url_analysis, text_analysis)

    return {
        "risk_score": total_score,
        "verdict": verdict,
        "explanations": explanations
    }

def get_explanations(url_result, text_result):
    reasons = []

    for rule, triggered in {**url_result, **text_result}.items():
        if triggered and rule in RULE_EXPLANATIONS:
            reasons.append(RULE_EXPLANATIONS[rule])

    return reasons
