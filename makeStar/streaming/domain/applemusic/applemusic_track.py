from __future__ import annotations


class AppleMusicTrack:
    def __init__(self,
                 id: str,
                 href: str | None,
                 type: str | None,
                 attributes: dict,
                 equivalents: dict,
                 relationships: dict
                 ):
        self.id = id
        self.href = href
        self.type = type
        self.attributes = attributes
        self.equivalents = equivalents
        self.relationships = relationships


