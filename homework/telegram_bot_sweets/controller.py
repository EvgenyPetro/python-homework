import random

import telebot
from telebot import types
import const

count_sweet = 221
max_step = 28
user_turn = 0
bot_turn = 0
flag = ""


def start():
    bot = telebot.TeleBot(const.TOKEN_ID)
    global flag

    @bot.message_handler(commands=['start'])
    def start_command(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but_new_games = types.KeyboardButton("Новая игра")
        but_options = types.KeyboardButton("Опции")
        markup.add(but_new_games, but_options)
        bot.send_message(message.chat.id, const.START_MESSAGE, reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def controller(message):
        global flag
        if message.text == "Новая игра":
            bot.send_message(message.chat.id, f"Всего в игре {count_sweet} конфет ")
            username = message.from_user.username
            flag = random.choice([username, "bot"])
            if flag == username:
                bot.send_message(message.chat.id, f"Первым ходит {username}")
                game_step(message)
            else:
                bot.send_message(message.chat.id, f"Первым ходит бот")
                game_step(message)

    def game_step(message):
        global flag
        global count_sweet
        if count_sweet > 0:
            if flag == message.from_user.username:
                bot.send_message(message.chat.id, f"Введите число от 1 до {max_step}")
                bot.register_next_step_handler(message, user_input)
            else:
                bot_input(message)
        else:
            flag = message.from_user.username if flag == "bot" else "bot"
            bot.send_message(message.chat.id, f"Победил {flag}")
            count_sweet = 221

    def bot_input(message):
        global count_sweet
        global bot_turn
        global flag
        bot_turn = (count_sweet % (max_step + 1))
        count_sweet -= bot_turn
        bot.send_message(message.chat.id, f"Бот взял {bot_turn} конфет")
        bot.send_message(message.chat.id, f"Осталось {count_sweet} конфет")
        flag = message.from_user.username if flag == "bot" else "bot"
        game_step(message)

    def user_input(message):
        global count_sweet
        global bot_turn
        global flag
        user_turn = int(message.text)
        count_sweet -= user_turn
        bot.send_message(message.chat.id, f"Осталось {count_sweet} конфет")
        flag = message.from_user.username if flag == "bot" else "bot"
        game_step(message)

    bot.infinity_polling()
