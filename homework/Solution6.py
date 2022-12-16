# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11
# - 2678 -> 34

number = input()
x = number.split(".")
sum = 0
left_number = int(x[0])

while (left_number != 0):
    sum = sum + left_number % 10
    left_number = left_number//10

if (len(x) == 2):
    right_number = int(x[1])
    while (right_number != 0):
        sum = sum + right_number % 10
        right_number = right_number//10


print(sum)
