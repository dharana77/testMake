import json

spotify_url = "/static/spotify.json"
spotify = json.loads(spotify_url)
appleMusic_url = "/static/appleMusic.json"


def test_get_spotify():
    spotify = get_spotify()
    assert len(spotify) != 0


def test_get_applemusic():
    applemusic = get_applemusic()
    assert len(applemusic) != 0


def is_converted_spotify_to_appleMusic():
    appleMusic = convert_spotify_to_appleMusic()
    assert appleMusic.to_json == json.loads(appleMusic_url)


def is_music_in_spotify_not_in_appleMusic():
    appleMusic = convert_spotify_to_appleMusic(spotify)
    assert appleMusic.to_json == json.loads(appleMusic_url)


def is_standard_country_US():
    appleMusic = convert_spotify_to_appleMusic()
    assert appleMusic.country == "US"


from django.test import TestCase

# Create your tests here.
