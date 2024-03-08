import json

from makeStar.errors import error_status
from makeStar.streaming.domain.applemusic.applemusic import AppleMusic
from makeStar.streaming.mock.fake_applemusic import FakeAppleMusicToTestAvailableCountries
from makeStar.streaming.mock.fake_spotify import FakeSpotifyToTestAvailableCountries

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
    apple_music = convert_spotify_to_applemusic()
    assert appleMusic.to_json == json.loads(appleMusic_url)


def test_is_music_in_spotify_but_not_exists_in_appleMusic():
    applemusic = AppleMusic()
    try:
        track_info = applemusic.search_apple_music_song("not exist song", "not exist artist")
    except Exception as e:
        assert e.__class__ == error_status.MusicNotExistInAppleMusic


def test_is_standard_country_US():
    appleMusic = convert_spotify_to_applemusic()
    assert appleMusic["track_information"]["available_countries"][0] == "US"


def test_can_switch_to_another_country_exist_in_available_countries():
    spotify = FakeSpotifyToTestAvailableCountries({"available_countries: ['US', 'KR']", "track_info: {'name': 'songname'}"})
    applemusic = FakeAppleMusicToTestAvailableCountries({"available_countries: ['US', 'KR', 'AU', 'EG']", "track_info: {'name': 'songname'}"})
    convert_country()
    assert applemusic.default_country in spotify.available_countries


def test_block_switch_to_another_country_not_exist_in_available_countries():
    spotify = FakeSpotifyToTestAvailableCountries({"available_countries: ['US']", "track_info: {'name': 'songname'}"})
    applemusic = FakeAppleMusicToTestAvailableCountries({"available_countries: ['US', 'KR', 'AU', 'EG']", "track_info: {'name': 'songname'}"})

    try:
        convert_country()
    except Exception as e:
        assert e.__class__ == error_status.COUNTRY_DOES_NOT_EXIST_IN_AVAILABLE_COUNTRIES

