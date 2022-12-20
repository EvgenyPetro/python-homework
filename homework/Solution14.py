# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def to_binary(digit):
    list_bit = []

    while digit != 0:
        list_bit.append(digit % 2)
        digit = digit // 2
    print(*list_bit[::-1], sep='')


to_binary(45)
to_binary(3)
to_binary(2)
