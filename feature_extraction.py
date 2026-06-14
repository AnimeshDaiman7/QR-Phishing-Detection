import re
import tldextract
import whois

def has_ip(url):
    pattern = r'(\d{1,3}\.){3}\d{1,3}'
    return 1 if re.search(pattern, url) else 0

def extract_features(url):
    features = []

    # 1. URL Length
    features.append(len(url))

    # 2. Number of dots
    features.append(url.count('.'))

    # 3. Presence of @
    features.append(1 if '@' in url else 0)

    # 4. Presence of -
    features.append(1 if '-' in url else 0)

    # 5. Suspicious keywords
    suspicious = ['login', 'verify', 'secure', 'update', 'bank']
    features.append(1 if any(word in url.lower() for word in suspicious) else 0)

    # 6. Domain length
    domain = tldextract.extract(url).domain
    features.append(len(domain))

    # 7. WHOIS availability (host-based feature)
    features.append(0)

    # 8. IP address in URL (NEW)
    features.append(has_ip(url))

    # 9. HTTPS usage (NEW)
    features.append(1 if url.startswith("https") else 0)

    return features