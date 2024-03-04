from django.test import TestCase
import json

spotify_url = "/static/spotify.json"
spotify = json.loads(spotify_url)


def is_converted_spotify_to_appleMusic():
    appleMusic = convert_spotify_to_appleMusic()
    appleMusic_url = "/static/appleMusic.json"
    assert appleMusic.to_json == json.loads(appleMusic_url)


def is_music_in_spotify_not_in_appleMusic():
    appleMusic = convert_spotify_to_appleMusic()
    assert

def is_standard_country_US():
    assert spotify.country == "US"
    appleMusic = convert_spotify_to_appleMusic()
    assert appleMusic.country == "US"