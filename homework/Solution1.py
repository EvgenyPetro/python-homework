# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_of_weak = int(input("enter day of weak "))

if 0 < day_of_weak < 6:
    print("no")
elif 5 < day_of_weak <= 7:
    print("yes")
else:
    print("Bad day")
