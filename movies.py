"""Movies module"""
import requests
from globals import MOVIES_GENRES_URL, MOVIES_BY_GENRE_URL
from genre_translation import GENRE_TRANSLATION


def get_movie_genres():
    """Get movie genres"""
    response = requests.get(MOVIES_GENRES_URL)
    if response.status_code == 200:
        data = response.json()
        return {
            genre['id']: GENRE_TRANSLATION.get(
                genre['name'],
                genre['name']) for genre in data['genres']}
    return {}


def get_movies_by_genre(genre_id):
    """Get movies by genre"""
    response = requests.get(MOVIES_BY_GENRE_URL + genre_id)
    if response.status_code == 200:
        data = response.json()
        return [movie['title'] for movie in data['results']][:5]
    return ["Проблема при отриманні даних"]
