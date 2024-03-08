import requests
from streaming.auth import streaming_auth

from makeStar.errors import error_status
from makeStar.streaming.domain.abstract_basic_streaming import AbstractBasicStreaming


class AppleMusic(AbstractBasicStreaming):
    def __init__(self):
        self.token = streaming_auth.get_token()
        self.playlist = []
        self.track_information = {}
        self.headers = {"Authorization": f"Bearer {self.token}"}
        self.default_country = "US"

    def search_apple_music_by_song_and_artist(self, song: str, artist: str):
        """
            args:
                song = "Ditto"
                artist = "NewJeans"
        """
        url = "https://api.music.apple.com/v1/catalog/us/search"
        params = {
            "term": f"{song} {artist}",
            "types": "songs",
            "limit": 1
        }
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise error_status.MusicNotExistInAppleMusic

    def get_available_countries(self):
        return self.track_information["countries"]
