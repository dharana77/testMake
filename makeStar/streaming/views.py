import os.path

from django.shortcuts import render
from django.http import JsonResponse
from streaming.domain.applemusic.applemusic import AppleMusic
from streaming.domain.spotify.util.spotify_util import read_spotify_file
import json


def convert_spotify_to_applemusic(request):
    spotify = read_spotify_file("./static/spotify.json")
    applemusic = AppleMusic()
    response = applemusic.search_apple_music_song("Ditto", "NewJeans")
    print(response)
    if response is not None and response.status.code == 200:
        track_info = response.json()
        return JsonResponse(track_info)
    return JsonResponse({'error': 'Unable to fetch the track info from Spotify.'})
