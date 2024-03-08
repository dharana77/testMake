from makeStar.streaming.auth import streaming_auth
import abc


class AbstractBasicStreaming(abc):
    def __init__(self):
        self.requestUrl = ""
        self.token = streaming_auth.get_token()
        self.default_country = "US"