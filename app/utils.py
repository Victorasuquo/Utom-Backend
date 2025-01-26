import requests

def verify_google_token(token):
    url = f"https://oauth2.googleapis.com/tokeninfo?id_token={token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
