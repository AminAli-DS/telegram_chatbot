"""Telegram chatbot"""
import random
from telebot import types
import requests
import emoji
from globals import bot
from movies import get_movie_genres, get_movies_by_genre
from tv import get_tv_by_genre, get_tv_genres
from music import get_music_genres, get_songs_by_genre

# Функції
def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return 'Нічия!'
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
         (user_choice == 'scissors' and bot_choice == 'paper') or \
         (user_choice == 'paper' and bot_choice == 'rock'):
        return 'Ви виграли!'
    else:
        return 'Ви програли!'


def load_jokes_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines() if line.strip()]


JOKES = load_jokes_from_file("./jokes.txt")


def get_random_joke():
    return random.choice(JOKES)


def get_random_quote():
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f'"{data["content"]}" - {data["author"]}'
    return "Проблема при отриманні цитати"


# Команда /start, головне меню бота
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton(
        emoji.emojize("🎬 Фільми"), callback_data='btn1')
    itembtn2 = types.InlineKeyboardButton(
        emoji.emojize("📺 Серіали"), callback_data='btn2')
    itembtn3 = types.InlineKeyboardButton(
        emoji.emojize("🎵 Музика"), callback_data='btn3')
    itembtn4 = types.InlineKeyboardButton(
        emoji.emojize("🎮 Ігри"), callback_data='btn4')
    itembtn5 = types.InlineKeyboardButton(
        emoji.emojize("😂 Анекдоти"), callback_data='btn5')
    itembtn6 = types.InlineKeyboardButton(
        emoji.emojize("📖 Цитати"), callback_data='btn6')

    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.send_message(message.chat.id, "Головне меню:", reply_markup=markup)


# Опрацювання запитів з кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "btn1":
        movie_genres = get_movie_genres()
        markup = types.InlineKeyboardMarkup(row_width=2)
        for genre_id, genre_name in movie_genres.items():
            markup.add(
                types.InlineKeyboardButton(
                    genre_name,
                    callback_data=f'movie_genre_{genre_id}'))
        markup.add(
            types.InlineKeyboardButton(
                'Повернутися',
                callback_data='main_menu'))
        bot.send_message(
            call.message.chat.id,
            "Оберіть жанр фільму:",
            reply_markup=markup)
    elif "movie_genre_" in call.data:
        genre_id = call.data.split('_')[2]
        movies = get_movies_by_genre(genre_id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton(
                'Повернутися',
                callback_data='main_menu'))
        bot.send_message(
            call.message.chat.id,
            "\n".join(movies),
            reply_markup=markup)
    elif call.data == "btn2":
        tv_genres = get_tv_genres()
        markup = types.InlineKeyboardMarkup(row_width=2)
        for genre_id, genre_name in tv_genres.items():
            markup.add(
                types.InlineKeyboardButton(
                    genre_name,
                    callback_data=f'tv_genre_{genre_id}'))
        markup.add(
            types.InlineKeyboardButton(
                'Повернутися',
                callback_data='main_menu'))
        bot.send_message(
            call.message.chat.id,
            "Оберіть жанр серіалу:",
            reply_markup=markup)
    elif "tv_genre_" in call.data:
        genre_id = call.data.split('_')[2]
        tv_shows = get_tv_by_genre(genre_id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton(
                'Повернутися',
                callback_data='main_menu'))
        bot.send_message(
            call.message.chat.id,
            "\n".join(tv_shows),
            reply_markup=markup)
    elif call.data == "btn3":
        music_genres = get_music_genres()
        markup = types.InlineKeyboardMarkup(row_width=2)
        for genre_id, genre_name in music_genres.items():
            markup.add(
                types.InlineKeyboardButton(
                    genre_name,
                    callback_data=f'music_genre_{genre_id}'))
        markup.add(
            types.InlineKeyboardButton(
                'Повернутися',
                callback_data='main_menu'))
        bot.send_message(
            call.message.chat.id,
            "Оберіть музичний жанр:",
            reply_markup=markup)
    elif "music_genre_" in call.data:
        genre_id = call.data.split('_')[2]
        songs = get_songs_by_genre(genre_id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton(
                'Повернутися',
                callback_data='main_menu'))
        bot.send_message(
            call.message.chat.id,
            "\n".join(songs),
            reply_markup=markup)

    elif call.data == "btn4":

        markup = types.InlineKeyboardMarkup(row_width=1)

        start_game_btn = types.InlineKeyboardButton(
            'Камінь-ножиці-папір', callback_data='rps_start')

        markup.add(start_game_btn)

        bot.send_message(
            call.message.chat.id,
            "Оберіть гру:",
            reply_markup=markup)

    elif call.data == 'rps_start':

        markup = types.InlineKeyboardMarkup(row_width=2)

        rock_btn = types.InlineKeyboardButton(
            'Камінь', callback_data='rps_rock')

        scissors_btn = types.InlineKeyboardButton(
            'Ножиці', callback_data='rps_scissors')

        paper_btn = types.InlineKeyboardButton(
            'Папір', callback_data='rps_paper')

        markup.add(rock_btn, scissors_btn, paper_btn)

        bot.send_message(
            call.message.chat.id,
            "Оберіть один із варіантів:",
            reply_markup=markup)

    elif call.data.startswith('rps_') and call.data != 'rps_start':

        user_choice = call.data.split('_')[1]

        bot_choice = random.choice(['rock', 'scissors', 'paper'])

        result = determine_winner(user_choice, bot_choice)

        bot_choice_translation = {

            'rock': 'Камінь',

            'scissors': 'Ножиці',

            'paper': 'Папір'

        }

        bot.send_message(
            call.message.chat.id,
            f"Ваш вибір: {bot_choice_translation[user_choice]}\n"
            f"Вибір бота: {bot_choice_translation[bot_choice]}\n\n{result}")

    elif call.data == "btn5":

        joke = get_random_joke()

        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(
            types.InlineKeyboardButton(
                'Ще один',
                callback_data='another_joke'))

        markup.add(
            types.InlineKeyboardButton(
                'Повернутися',
                callback_data='main_menu'))

        bot.send_message(call.message.chat.id, joke, reply_markup=markup)

    elif call.data == "another_joke":
        joke = get_random_joke()
        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(
            types.InlineKeyboardButton(
                'Ще один',
                callback_data='another_joke'))
        markup.add(
            types.InlineKeyboardButton(
                'Повернутися',
                callback_data='main_menu'))

        bot.send_message(call.message.chat.id, joke, reply_markup=markup)

    elif call.data == "btn6":

        quote = get_random_quote()

        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(
            types.InlineKeyboardButton(
                'Ще одну',
                callback_data='another_quote'))

        markup.add(
            types.InlineKeyboardButton(
                'Повернутися',
                callback_data='main_menu'))

        bot.send_message(call.message.chat.id, quote, reply_markup=markup)

    elif call.data == "another_quote":
        quote = get_random_quote()
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton(
                'Ще одну',
                callback_data='another_quote'))
        markup.add(
            types.InlineKeyboardButton(
                'Повернутися',
                callback_data='main_menu'))
        bot.send_message(call.message.chat.id, quote, reply_markup=markup)

    elif call.data == "main_menu":
        markup = types.InlineKeyboardMarkup(row_width=2)
        itembtn1 = types.InlineKeyboardButton(
            emoji.emojize("🎬 Фільми"), callback_data='btn1')
        itembtn2 = types.InlineKeyboardButton(
            emoji.emojize("📺 Серіали"), callback_data='btn2')
        itembtn3 = types.InlineKeyboardButton(
            emoji.emojize("🎵 Музика"), callback_data='btn3')
        itembtn4 = types.InlineKeyboardButton(
            emoji.emojize("🎮 Ігри"), callback_data='btn4')
        itembtn5 = types.InlineKeyboardButton(
            emoji.emojize("😂 Анекдоти"), callback_data='btn5')
        itembtn6 = types.InlineKeyboardButton(
            emoji.emojize("📖 Цитати"), callback_data='btn6')

        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
        bot.send_message(
            call.message.chat.id,
            "Головне меню:",
            reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
