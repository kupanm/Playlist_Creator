"""
1: Log Into Youtube
2: Grab Liked Videos (possibly if type music ID (10))
3: Create a New Playlist
4: Search for the song
5: Add the song to the Spotify Playlist
"""

from googleapiclient.discovery import build
import os



api_key = os.environ.get("YT_API_KEY")
print(api_key)


youtube = build('youtube',
                'v3',
                developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    forUsername='schafer5'
)

request = request.execute()