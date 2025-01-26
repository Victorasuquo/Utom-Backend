import requests

def verify_google_token(token):
    url = f"https://oauth2.googleapis.com/tokeninfo?id_token={token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# import requests
# import os

# GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
# GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
# REDIRECT_URI = os.getenv("REDIRECT_URI", "http://localhost:5000/callback")


# def exchange_google_code(code):
#     """Exchange authorization code for access token."""
#     url = "https://oauth2.googleapis.com/token"
#     payload = {
#         "code": code,
#         "client_id": GOOGLE_CLIENT_ID,
#         "client_secret": GOOGLE_CLIENT_SECRET,
#         "redirect_uri": REDIRECT_URI,
#         "grant_type": "authorization_code",
#     }
#     response = requests.post(url, data=payload)
#     if response.status_code == 200:
#         return response.json()
#     return None


# def get_user_info(access_token):
#     """Retrieve user information using access token."""
#     url = "https://www.googleapis.com/oauth2/v2/userinfo"
#     headers = {"Authorization": f"Bearer {access_token}"}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     return None
