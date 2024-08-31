"""
1: Log Into Youtube
2: Grab Liked Videos (possibly if type music ID (10))
3: Create a New Playlist
4: Search for the song
5: Add the song to the Spotify Playlist
"""
#project_env\Scripts\activate.bat


import os

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import googleapiclient.errors


class YoutubeCall():
    def __init__(self):
        self.scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.client_secrets_file = "clients_secrets.json"

    def api_call(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        flow = InstalledAppFlow.from_client_secrets_file(
            self.client_secrets_file, self.scopes)
        credentials = flow.run_local_server()
        youtube = build(
            self.api_service_name, self.api_version, credentials=credentials)

        request = youtube.videos().list(
            part="snippet,contentDetails",
            myRating="like"
        )
        return request
    
    def filter_response(self, response):
        liked_music_videos = []
        videos = response['items']
        for video in videos:
            if video['snippet']['categoryId'] == '10': # video is of category music
                liked_music_videos.append((video['snippet']['title'], video['snippet']['channelTitle']))
        return liked_music_videos


youtube = YoutubeCall()
response = youtube.api_call().execute()

filtered = youtube.filter_response(response)

print(filtered)