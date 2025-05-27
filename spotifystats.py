import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
import os

load_dotenv('config.env')

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
if not client_id or not client_secret or not redirect_uri:
    raise ValueError("Please set SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, and SPOTIPY_REDIRECT_URI in your .env file.")

TRACK_FILTER = 2 * 60 * 1000  # 2 minutes
UNIQUE_TRACKS_LIMIT = 50

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="user-read-recently-played user-top-read"
))

unique_tracks = {}
before = None

# 1. Get recently played tracks (paginated)
while len(unique_tracks) < UNIQUE_TRACKS_LIMIT:
    results = sp.current_user_recently_played(limit=50, before=before)
    items = results.get('items', [])
    if not items:
        break

    for item in items:
        track = item['track']
        track_id = track['id']
        duration = track['duration_ms']

        if duration < TRACK_FILTER and track_id not in unique_tracks:
            unique_tracks[track_id] = {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'duration_ms': duration,
                'url': track['external_urls']['spotify']
            }
            if len(unique_tracks) >= UNIQUE_TRACKS_LIMIT:
                break

    before = items[-1]['played_at']

# 2. If still not enough, get top tracks (medium term)
if len(unique_tracks) < UNIQUE_TRACKS_LIMIT:
    results = sp.current_user_top_tracks(limit=50, time_range='medium_term')

    for track in results['items']:
        track_id = track['id']
        duration = track['duration_ms']

        if duration < TRACK_FILTER and track_id not in unique_tracks:
            unique_tracks[track_id] = {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'duration_ms': duration,
                'url': track['external_urls']['spotify']
            }
            if len(unique_tracks) >= UNIQUE_TRACKS_LIMIT:
                break

# Print final list
for track in unique_tracks.values():
    print(f"{track['name']} by {track['artist']} ({track['duration_ms'] / 1000:.2f} seconds)")
    print(f"Track URL: {track['url']}")
    print("--------------------------------------------------")
