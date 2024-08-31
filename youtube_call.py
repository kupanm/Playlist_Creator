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

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
   # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "clients_secrets.json"

    # Get credentials and create an API client
    flow = InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().list(
        part="snippet,contentDetails",
        myRating="like"
    )
    response = request.execute()

    # print(response)
    
    videos = response['items']
    # print(videos)
    
    liked_music_videos = []
    for video in videos:
        if video['snippet']['categoryId'] == '10': # video is of category music
            liked_music_videos.append((video['snippet']['title'], video['snippet']['channelTitle']))

    print(liked_music_videos)
if __name__ == '__main__':
    main()