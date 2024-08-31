"""
4: Search for the song
5: Add the song to the Spotify Playlist

"""
import json
import os
from dotenv import load_dotenv
import base64
from requests import post

load_dotenv()

client_id = os.getenv("CLIENT_ID")

if not client_id:
    raise ValueError("No client ID found")

client_secret = os.getenv("CLIENT_SECRET")

if not client_secret:
    raise ValueError("No client secret found")

def get_token():
    auth_str = client_id + ":" + client_secret
    auth_bytes = auth_str.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    print(auth_base64)
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic" + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    # token = json_result["access_token"]
    return json_result

token = get_token()
print(token)
    