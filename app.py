import re

def is_phishing_url(url):
    # Rule 1: Contains IP address
    if re.match(r"http[s]?://\d+\.\d+\.\d+\.\d+", url):
        return True

    # Rule 2: Contains '@' symbol
    if '@' in url:
        return True

    # Rule 3: Contains '-' in domain (commonly used in phishing)
    if '-' in url:
        return True

    # Rule 4: Long URL
    if len(url) > 75:
        return True

    # Rule 5: Not using HTTPS
    if not url.startswith("https"):
        return True

    return False

# 🚀 Run the checker
url = input("Enter a URL to check: ")

if is_phishing_url(url):
    print("⚠️ Warning: This URL looks like a phishing link.")
else:
    print("✅ This URL appears to be safe.")
