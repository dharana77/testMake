from makeStar.streaming.auth import streaming_auth


class BasicStreaming():
    def __init__(self):
        self.requestUrl = ""
        self.token = streaming_auth.get_token()
