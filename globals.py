"""Global constants"""
import telebot

# Токен і API ключі
TOKEN = '6693729475:AAHlTQfNjNkwN6vYLhM67qiK473-Klwb5g0'
API_KEY = 'b1826c6059192a67e00a4e541e90b1fb'
BASE_URL = 'https://api.themoviedb.org/3'
DEEZER_URL = 'https://api.deezer.com'
COUNTRY_CODE = 'UA'
bot = telebot.TeleBot(TOKEN)

MOVIES_GENRES_URL = f'{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US'
MOVIES_BY_GENRE_URL = f'{BASE_URL}/discover/movie?api_key={API_KEY}&language=en-US&sort_by=popularity.desc&page=1&with_genres='

MUSIC_GENRES = f'{DEEZER_URL}/genre'
SONGS_BY_GENRE = f'/artists?country={COUNTRY_CODE}'


TV_GENRES_URL = f'{BASE_URL}/genre/tv/list?api_key={API_KEY}&language=en-US'
TV_BY_GENRE_URL = f'{BASE_URL}/discover/tv?api_key={API_KEY}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres='
