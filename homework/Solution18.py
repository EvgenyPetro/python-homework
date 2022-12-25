# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

list_old = []
for i in (range(20)):
    list_old.append(random.randint(1, 20))
print(list_old)


def not_double(list_element):
    new_list = []
    for elem in list_element:
        if elem not in new_list:
            new_list.append(elem)
    return new_list


print(not_double(list_old))
