import telebot
from telebot import types
import const
import datetime

a = 0
b = 0


def start():
    bot = telebot.TeleBot(const.TOKEN_ID)

    @bot.message_handler(commands=['start'])
    def start_command(message):
        START_MESSAGE = """
        С какими числами будем работать?
        """
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rac_number_btn = types.KeyboardButton("Рациональные числа")
        com_number_btn = types.KeyboardButton("Комплексные числа")
        markup.add(rac_number_btn, com_number_btn)
        bot.send_message(message.chat.id, START_MESSAGE, reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def number_variant(message):
        if message.text == "Рациональные числа":
            bot.send_message(message.chat.id, "Введите два числа через пробел")
            log(message)
            bot.register_next_step_handler(message, user_input_number)
        elif message.text == "Комплексные числа":
            bot.send_message(message.chat.id, "Введите числа через пробел.")
            log(message)
            bot.register_next_step_handler(message, user_input_complex_number)

    def user_input_number(message):
        global a, b
        log(message)
        numbers = message.text
        a = int(numbers.split()[0])
        b = int(numbers.split()[1])
        input_operation_rac(message)

    def user_input_complex_number(message):
        global a, b
        log(message)
        numbers = message.text
        a = complex(numbers.split()[0])
        b = complex(numbers.split()[1])
        input_operation_complex(message)

    def input_operation_rac(message):
        markupp = types.ReplyKeyboardMarkup(resize_keyboard=True)
        plus_btn = types.KeyboardButton("+")
        minus_btn = types.KeyboardButton("-")
        multy_btn = types.KeyboardButton("*")
        div_btn = types.KeyboardButton("/")
        div_cel_btn = types.KeyboardButton("//")
        div_ost_btn = types.KeyboardButton("%")
        markupp.row(plus_btn, minus_btn, multy_btn, div_btn)
        markupp.row(div_cel_btn, div_ost_btn)
        bot.send_message(message.chat.id, "Введите знак с клавиатуры", reply_markup=markupp)
        bot.register_next_step_handler(message, operations)

    def input_operation_complex(message):
        markupp = types.ReplyKeyboardMarkup(resize_keyboard=True)
        plus_btn = types.KeyboardButton("+")
        minus_btn = types.KeyboardButton("-")
        multy_btn = types.KeyboardButton("*")
        div_btn = types.KeyboardButton("/")
        markupp.row(plus_btn, minus_btn)
        markupp.row(multy_btn, div_btn)
        bot.send_message(message.chat.id, "Введите знак с клавиатуры", reply_markup=markupp)
        bot.register_next_step_handler(message, operations)

    @bot.message_handler(content_types=["text"])
    def operations(message):
        global a, b
        log(message)
        result = 0
        if message.text == "+":
            result = a + b
            bot.send_message(message.chat.id, f'{a} + {b} = {result}')
        elif message.text == "-":
            result = a - b
            bot.send_message(message.chat.id, f'{a} - {b} = {result}')
        elif message.text == "*":
            result = a * b
            bot.send_message(message.chat.id, f'{a} * {b} = {result}')
        elif message.text == "/":
            result = a / b
            bot.send_message(message.chat.id, f'{a} / {b} = {result}')
        elif message.text == "%":
            result = a % b
            bot.send_message(message.chat.id, f'{a} % {b} = {result}')
        elif message.text == "//":
            result = a // b
            bot.send_message(message.chat.id, f'{a} // {b} = {result}')

    def log(message):
        file = open('logs.csv', 'a')
        file.write(f'{datetime.datetime.now()},{message.chat.username},{message.text}\n')
        file.close()

    bot.infinity_polling()
