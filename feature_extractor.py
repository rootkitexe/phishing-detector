import re
import tldextract
import whois
from urllib.parse import urlparse

def extract_features(url):
    features = {}
    features['url_length'] = len(url)

    # Use of IP
    features['uses_ip'] = 1 if re.match(r"https?://\d{1,3}(\.\d{1,3}){3}", url) else 0

    # @ symbol
    features['has_at_symbol'] = 1 if '@' in url else 0

    # Subdomains
    ext = tldextract.extract(url)
    subdomain = ext.subdomain.split('.')
    features['num_subdomains'] = len([s for s in subdomain if s])

    # Hyphen
    features['has_hyphen'] = 1 if '-' in url else 0

    # HTTPS
    features['uses_https'] = 1 if url.startswith("https") else 0

    # WHOIS age
    try:
        domain_info = whois.whois(ext.domain + "." + ext.suffix)
        if domain_info.creation_date and domain_info.expiration_date:
            age = (domain_info.expiration_date - domain_info.creation_date).days
            features['domain_age'] = age
        else:
            features['domain_age'] = -1
    except:
        features['domain_age'] = -1

    return features
