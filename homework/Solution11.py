# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_int = [2, 3, 5, 9, 3]


def sum_odd_element(list_element):
    sum_odd = 0
    for i in range(1, len(list_element), 2):
        sum_odd += list_element[i]
    return sum_odd


print(sum_odd_element(list_int))
