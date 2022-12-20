# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def nega_fib(n):
    if n <= 0:
        return [0]
    else:
        left = [0, 1]
        right = [0, 1]
        for i in range(2, n + 1):
            b = right[i - 1] + right[i - 2]
            right.append(b)
            c = (right[i - 1] + right[i - 2]) * (-1) ** (i + 1)
            left.append(c)
        return left[-1:0:-1] + right


n = 8
print(nega_fib(n))
