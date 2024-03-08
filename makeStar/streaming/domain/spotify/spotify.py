from makeStar.streaming.auth import streaming_auth
import requests

from makeStar.streaming.domain.abstract_basic_streaming import AbstractBasicStreaming


class Spotify(AbstractBasicStreaming):
    def __init__(self):
        self.playlist = []
        self.track_information = {}
        #TODO add token and header
        """
        self.token = streaming_auth.get_token()
        self.headers = {"Authorization": f"Bearer {self.token}"}
        """

    def get_playlist_tracks(self, playlist):
        res = {}
        for playlist_id in playlist:
            url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                res[playlist_id] = response.json()
            else:
                res[playlist_id] = None
        return res

    def get_available_countries(self):
        return self.track_information["countries"]
