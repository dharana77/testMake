from makeStar.streaming.mock.fake_streaming import FakeStreaming


class FakeSpotifyToTestAvailableCountries(FakeStreaming):
    def __init__(self, track_info):
        track_info = {}