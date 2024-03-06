from __future__ import annotations


class SpotifyAlbum:
    def __init__(self,
                 id: str,
                 uri: str | None,
                 href: str| None,
                 name: str | None,
                 type: str | None,
                 artists: list,
                 album_type: str | None,
                 release_date: str | None,
                 total_tracks: int,
                 external_urls: dict,
                 available_markets: list,
                 explicit: bool,
                 is_local: bool,
                 popularity: int,
                 disc_number: int,
                 duration_ms: int,
                 preview_url: str | None,
                 external_ids: dict,
                 track_number: int,
                ):

        self.id = id
        self.uri = uri
        self.href = href
        self.name = name
        self.type = type
        self.artists = artists
        self.album_tpe = album_type
        self.release_date = release_date
        self.total_tracks = total_tracks
        self.external_urls = external_urls
        self.available_markets = available_markets
        self.explicit = explicit
        self.is_local = is_local
        self.popularity = popularity
        self.disc_number = disc_number
        self.duration_ms = duration_ms
        self.preview_url = preview_url
        self.external_ids = external_ids
        self.track_number = track_number
