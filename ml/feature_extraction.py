import re
import math
import tldextract

from collections import Counter
from urllib.parse import urlparse


def calculate_entropy(text):

    counter = Counter(text)

    length = len(text)

    entropy = 0

    for count in counter.values():

        probability = count / length

        entropy -= probability * math.log2(probability)

    return entropy


def extract_features(url):

    # Normalize URL
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    extracted = tldextract.extract(url)

    try:
        parsed = urlparse(url)
    except Exception:
        parsed = urlparse("")

    domain = extracted.domain

    # Suspicious Keywords
    keywords = [
        "login",
        "verify",
        "update",
        "secure",
        "account",
        "bank",
        "paypal",
        "amazon",
        "signin",
        "password"
    ]

    keyword_count = sum(
        1 for keyword in keywords
        if keyword in url.lower()
    )

    # Suspicious TLDs
    suspicious_tlds = {
        "tk",
        "ml",
        "ga",
        "cf",
        "gq"
    }

    suspicious_tld = (
        1
        if extracted.suffix in suspicious_tlds
        else 0
    )

    # Path Depth
    path_depth = len(
        [part for part in parsed.path.split("/")
         if part]
    )

    # URL Entropy
    entropy = calculate_entropy(url)

    features = {

        # Existing Features
        "url_length": len(url),

        "dot_count": url.count("."),

        "hyphen_count": url.count("-"),

        "digit_count": sum(
            c.isdigit()
            for c in url
        ),

        "slash_count": url.count("/"),

        "question_count": url.count("?"),

        "equal_count": url.count("="),

        "ampersand_count": url.count("&"),

        "at_symbol":
            1 if "@" in url else 0,

        "https":
            1 if url.startswith("https")
            else 0,

        "domain_length":
            len(domain),

        "subdomain_count":
            len(extracted.subdomain.split("."))
            if extracted.subdomain
            else 0,

        "ip_present":
            1 if re.search(
                r'(\d{1,3}\.){3}\d{1,3}',
                url
            )
            else 0,

        # New Features
        "keyword_count":
            keyword_count,

        "suspicious_tld":
            suspicious_tld,

        "path_depth":
            path_depth,

        "entropy":
            entropy
    }

    return features