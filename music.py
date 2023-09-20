"""Music module"""
import requests
from globals import MUSIC_GENRES, SONGS_BY_GENRE


def get_music_genres():
    """Get music genres"""
    response = requests.get(MUSIC_GENRES)
    if response.status_code == 200:
        return {genre['id']: genre['name']

    for genre in response.json()['data']}  # what is this line for?
    return {}


def get_songs_by_genre(genre_id):
    """Get songs by genre"""
    response = requests.get(f'{MUSIC_GENRES}/{genre_id}{SONGS_BY_GENRE}')
    if response.status_code == 200:
        return [song['name']

    for song in response.json()['data']][:5]  
    return ["Проблема при отриманні даних"]
