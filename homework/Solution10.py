# Реализуйте алгоритм перемешивания списка.

import random

list = [1,4,7,3,7,3,6,8,3,1,4,10]
new_list=[]
for i in range(len(list)):
    pos = random.randint(0,len(list)-1)
    new_list.append(list[pos])
    list.remove(list[pos])

print(new_list)