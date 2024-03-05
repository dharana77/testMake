


def test_get_spotify():
    spotify = get_spotify()
    assert len(spotify) != 0


def test_get_applemusic():
    applemusic = get_applemusic()
    assert len(applemusic) != 0