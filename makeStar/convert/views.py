from django.shortcuts import render
import json


def convert_spotify_to_applemusic():
    spotify = json.loads("/static/spotify")
    return spotify