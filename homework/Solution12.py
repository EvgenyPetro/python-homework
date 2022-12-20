# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_element1 = [2, 3, 4, 5, 6]
list_element2 = [2, 3, 5, 6]


def multi_first_last_element(list_elements):
    new_list = []
    for i in range(len(list_elements) // 2 + 1):
        mid = len(list_elements) / 2
        if i < mid:
            first, last = list_elements[i], list_elements[len(list_elements) - i - 1]
            new_list.append(first * last)
    return new_list


print(multi_first_last_element(list_element1))
print(multi_first_last_element(list_element2))
