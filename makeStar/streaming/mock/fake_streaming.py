import abc

from makeStar.streaming.domain.abstract_basic_streaming import AbstractBasicStreaming


class FakeStreaming(AbstractBasicStreaming):
    def __init__(self):
        url = ""
        track_info = {}