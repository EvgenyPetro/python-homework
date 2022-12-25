# Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint


def create_fun(k):
    string = []
    for i in range(k, -1, -1):
        a = randint(0, 100)
        if a == 1:
            if i == 0:
                string.append(f'{a}')
            elif i == 1:
                string.append(f'x')
            else:
                string.append(f'x^{i}')
        elif a != 0:
            if i == 0:
                string.append(f'{a}')
            elif i == 1:
                string.append(f'{a}*x')
            else:
                string.append(f'{a}*x^{i}')

    return (f'{" + ".join(string)} = 0')


k = 3
with open('homework19.txt', 'w') as f:
    f.write(create_fun(k))
