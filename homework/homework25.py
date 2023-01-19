# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first_element = int(input("Введите первый элемент прогрессии: "))
difference = int(input("Введите разность прогрессии: "))
count_elements = int(input("Введите количество элементов прогрессии: "))


def get_arr(first, diff, count):
    return [first + (i - 1) * diff for i in range(1, count + 1)]


print(get_arr(first_element, difference, count_elements))
