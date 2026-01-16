import re

def has_ip_address(url):
    ip_pattern = r"(?:\d{1,3}\.){3}\d{1,3}"
    return bool(re.search(ip_pattern, url))

def has_suspicious_tld(url):
    suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq']
    return any(tld in url.lower() for tld in suspicious_tlds)

def uses_https(url):
    return url.lower().startswith("https://")

def is_long_url(url, threshold=75):
    return len(url) > threshold

def analyze_url(url):
    return {
        "ip_in_url": has_ip_address(url),
        "suspicious_tld": has_suspicious_tld(url),
        "uses_https": uses_https(url),
        "long_url": is_long_url(url)
    }


