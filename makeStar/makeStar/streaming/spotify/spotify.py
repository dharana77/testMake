from makeStar.makeStar.auth import streaming_auth


class Spotify:
    def __init__(self):
        self.token = streaming_auth.get_token()
        self.playlist = []
        self.track_information = {}
