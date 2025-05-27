# Spotify Short Tracks Collector

This Python script fetches your Spotify listening history and top tracks to find up to 50 unique tracks under 2 minutes in duration. It’s designed to help with [Music League](https://www.musicleague.com/) competitions where short tracks are often favored.

## Features

- Uses Spotify API to get recently played tracks and top tracks.
- Filters for tracks shorter than 2 minutes.
- Combines results and removes duplicates.
- Outputs track name, artist, duration, and Spotify URL.

## Setup

### 1. Create a Spotify Developer Application

- Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)
- Create an app to get your `CLIENT_ID` and `CLIENT_SECRET`.
- Set the Redirect URI to `http://0.0.0.0:8888/callback` (or your preferred redirect URL).

### 2. Clone this repo

```bash
git clone https://github.com/Voidfaller/SpotifyStats.git
cd SpotifyStats
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Fill in the Dummy config.env with your api credentials
```.env
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
SPOTIPY_REDIRECT_URI=your_redirect_uri_here
```

### 5. Run the Script

```bash
python spotifystats.py
```
