"""
4: Search for the song
5: Add the song to the Spotify Playlist

"""
import os


client_id = os.environ.get("test")

if not client_id:
    raise ValueError("No client ID found")

print(client_id)
# client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

# if not client_secret:
#     raise ValueError("No client secret found")


print(client_id)

# print(client_secret)