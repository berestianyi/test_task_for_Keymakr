import requests

def fetch_users(url: str) -> list[dict]:
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    data = r.json()
    if not isinstance(data, list):
        raise ValueError("Expected a list of users")
    return data