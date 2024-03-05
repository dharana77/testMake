
class AppleMusicTrackAttributes:
    def __init__(self,
                 url: str,
                 isrc: str,
                 name: str,
                 artwork: dict,
                 preview: list,
                 album_name: str,
                 has_lyrics: bool,
                 artist_name: str,
                 disc_number: int,
                 genre_names: list,
                 has_credits: bool,
                 play_params: dict,
                 release_date: str,
                 track_number: int,
                 duration_in_mills: int,
                 is_apple_digital_master: bool
                 ):
        self.url = url
        self.isrc: isrc
        self.name = name
        self.artwork = artwork
        self.preview = preview
        self.album_name = album_name
        self.has_lyrics = has_lyrics
        self.artist_name = artist_name
        self.disc_number = disc_number
        self.genre_names: genre_names
        self.has_credits = has_credits
        self.play_params = play_params
        self.release_date = release_date
        self.track_number = track_number
        self.duration_in_mills = duration_in_mills
        self.is_apple_digital_master = is_apple_digital_master