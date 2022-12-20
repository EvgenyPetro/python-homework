# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

list_element = []
for i in range(10):
    list_element.append(round(random.uniform(10, 20), random.randint(0, 3)))
print(list_element)


def difference(list_elements):
    new_list = []

    for i in list_elements:
        right_part = i - int(i)
        if right_part != 0:
            new_list.append(right_part)

    max_element, min_element = max(new_list), min(new_list)
    return round((max_element - min_element), 3)


print(difference(list_element))
