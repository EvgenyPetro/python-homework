# Задайте список из n чисел последовательности (1+1\n)^n и выведите на экран их сумму.

# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

n = int(input())
a = {i: (1+1/i)**i for i in range(1, n+1)}
sum = 0
for i in a.values():
    sum = sum + i
print(format(sum, ".2f"))
