def normalize_text(text):
    return text.lower()

def has_urgency(text):
    urgency_words = [
        "urgent", "immediately", "act now",
        "limited time", "asap"
    ]
    return any(word in text for word in urgency_words)

def has_threat(text):
    threat_words = [
        "account suspended", "account locked",
        "security alert", "unusual activity",
        "verify immediately"
    ]
    return any(word in text for word in threat_words)

def has_reward(text):
    reward_words = [
        "you won", "congratulations",
        "free", "cashback", "gift"
    ]
    return any(word in text for word in reward_words)

def analyze_text(text):
    text = normalize_text(text)
    return {
        "urgency_detected": has_urgency(text),
        "threat_detected": has_threat(text),
        "reward_detected": has_reward(text)
    }



