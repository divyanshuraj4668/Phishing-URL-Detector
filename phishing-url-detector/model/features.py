import re
from urllib.parse import urlparse

SUSPICIOUS_WORDS = {
    "login", "verify", "verification", "secure", "account", "update",
    "confirm", "password", "bank", "signin", "security", "free",
    "bonus", "claim", "wallet", "payment"
}

def _normalise_url(url):
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url):
        return "http://" + url
    return url

def _is_ip(hostname):
    if not hostname:
        return 0
    return int(bool(re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", hostname)))

def extract_features(url):
    url = _normalise_url(url)
    parsed = urlparse(url)
    hostname = parsed.netloc.split("@")[-1].split(":")[0]
    path = parsed.path or ""
    lower = url.lower()

    words_found = sum(word in lower for word in SUSPICIOUS_WORDS)

    return {
        "url_length": len(url),
        "hostname_length": len(hostname),
        "path_length": len(path),
        "dot_count": url.count("."),
        "hyphen_count": url.count("-"),
        "at_count": url.count("@"),
        "question_count": url.count("?"),
        "equal_count": url.count("="),
        "slash_count": url.count("/"),
        "digit_count": sum(c.isdigit() for c in url),
        "subdomain_count": max(0, len(hostname.split(".")) - 2),
        "has_https": int(parsed.scheme.lower() == "https"),
        "has_ip_address": _is_ip(hostname),
        "has_suspicious_word": int(words_found > 0)
    }
