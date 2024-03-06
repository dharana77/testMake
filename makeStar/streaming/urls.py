from django.contrib import admin
from django.urls import path
from streaming import views

urlpatterns = [
    path('applemusic', views.convert_spotify_to_applemusic, name="applemusic"),
]
