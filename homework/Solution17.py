# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def get_simpl_multi(n):
    multi = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            multi.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        multi.append(n)
    return multi


a = 1
print(get_simpl_multi(a))
a = 2
print(get_simpl_multi(a))
a = 9
print(get_simpl_multi(a))
a = 13
print(get_simpl_multi(a))
a = 30
print(get_simpl_multi(a))
