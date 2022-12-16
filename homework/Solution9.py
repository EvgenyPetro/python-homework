# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# n = int(input())
import random


n = int(input())

list = []
for i in range(n):
    list.append(random.randint(-n, n))
print(list)

file = open('file.txt','r')
one_element = int(file.readline())
two_element = int(file.readline())
file.close()

if(0<one_element<n and 0<two_element<n):
    multi = list[one_element]*list[two_element]
    print(multi)
else:
    print("error")