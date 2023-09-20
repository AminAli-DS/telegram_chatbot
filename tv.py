"""TV module"""
import requests
from globals import TV_GENRES_URL, TV_BY_GENRE_URL
from genre_translation import GENRE_TRANSLATION

def get_tv_genres():
    """Get TV genres"""
    response = requests.get(TV_GENRES_URL)
    if response.status_code == 200:
        data = response.json()
        return {
            genre['id']: GENRE_TRANSLATION.get(
                genre['name'],
                genre['name']) for genre in data['genres']}
    return {}


def get_tv_by_genre(genre_id):
    """Get TV by genre"""
    response = requests.get(TV_BY_GENRE_URL + genre_id)
    if response.status_code == 200:
        data = response.json()
        return [tv['name'] for tv in data['results']][:5]
    return ["Проблема при отриманні даних"]
