# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#    a) Добавьте игру против бота
#    b) Подумайте как наделить бота ""интеллектом""
import random


def who_begins():
    rand = random.randint(1, 2)
    if rand == 1:
        flag = True
    else:
        flag = False
    return flag


def is_digit(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def difference_number(text, max_step):
    number = input(f"{text}")
    while True:
        if is_digit(number):
            number = int(number)
            if 1 <= number <= max_step:
                return number
        number = input(f"Введите число от 1 до {max_step}: ")


def who_winners(count, player):
    if count <= 0:
        if player:
            print("Winner: Player 2")
        else:
            print("Winner: Player 1")


def easy_bot_player(max_step):
    number = random.randint(1, max_step)
    print(f"Бот берет {number}")
    return number


def hard_bot_player(count, max_step):
    print(f"Бот берет {count % (max_step + 1)}")
    return count % (max_step + 1)




def game(count, max_step, game_mode, level_bot):
    player = who_begins()
    while count > 0:
        if player:
            a = difference_number("Ходит игрок 1: ", max_step)
            player = False

        else:
            if game_mode == 1:
                a = difference_number("Ходит игрок 2: ", max_step)
                player = True
            else:
                if level_bot == 1:
                    a = easy_bot_player(max_step)
                    player = True
                elif level_bot == 2:
                    a = hard_bot_player(count, max_step)
                    player = True
        count = count - a
        who_winners(count, player)
        print(count)


print('Добро пожаловать в игру "Забери конфеты"')
print('Выберете режим игры: ')
print('1. Игрок против игрока')
print('2. Игрок против бота')

game_mode = int(input())
level_bot = 1
if game_mode == 2:
    print("Введите уровень бота: ")
    print("1. Легкий ")
    print("2. Невозможный ")
    level_bot = int(input())

print('Введите количество общее количество конфет: ')
count = int(input())
print('Введите сколько конфет можно взять максимум одному игроку')
max_step = int(input())

game(count, max_step, game_mode, level_bot)
