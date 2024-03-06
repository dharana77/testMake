import json

from makeStar.streaming.domain.applemusic.applemusic import AppleMusic

spotify_url = "/static/spotify.json"
spotify = json.loads(spotify_url)
appleMusic_url = "/static/appleMusic.json"


def test_get_spotify():
    spotify = get_spotify()
    assert len(spotify) != 0


def test_get_applemusic():
    apple_music = get_applemusic()
    assert len(applemusic) != 0


def test_is_converted_spotify_to_appleMusic():
    apple_music = convert_spotify_to_apple_music()
    assert appleMusic.to_json == json.loads(appleMusic_url)


def test_is_music_in_spotify_but_not_exists_in_appleMusic():
    apple_music = AppleMusic()
    track_info = applemusic.search_apple_music_song("not exist song", "not exist artist")
    assert track_info is None


def test_is_standard_country_US():
    appleMusic = convert_spotify_to_appleMusic()
    assert appleMusic["track_information"]["available_countries"][0] == "US"
