"""
    1. Get all playlists
    2. Create a youtube liked music playlist (if it doesn't exist)
    3. Search for the songs that the youtube script returns
    4. Add those songs to the playlist
"""

import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('CLIENT_ID')
if not client_id:
    raise ValueError("NO CLIENT ID")

client_secret = os.getenv('CLIENT_SECRET')
if not client_secret:
    raise ValueError("NO CLIENT SECRET")

app_secret = os.getenv('APP_SECRET')
if not app_secret:
    raise ValueError("NO APP SECRET")


app = Flask(__name__)

app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'
app.secret_key = app_secret
TOKEN_INFO = 'token_info'

@app.route('/')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirect_page():
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('save_youtube_songs', external=True))


@app.route('/saveYoutubeSongs')
def save_youtube_songs():
    try:
        token_info = get_token()
    except:
        print("USER NOT LOGGED IN")
        return redirect('/')
    return("OAUTH SUCCESSFUL")

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login'), external=False)
    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if(is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info


def create_spotify_oauth():
    return SpotifyOAuth(client_id=client_id,
                        client_secret=client_secret,
                        redirect_uri=url_for('redirect_page', _external=True),
                        scope='user-library-read playlist-modify-public playlist-modify-private')


app.run(debug=True)