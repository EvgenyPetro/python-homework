# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math


def stepen(d):
    i = 0
    while d < 1:
        d *= 10
        i += 1
    return i


d = 0.00001
print(round(math.pi, stepen(d)))
d = 0.001
print(round(math.pi, stepen(d)))
d = 0.1
print(round(math.pi, stepen(d)))
d = 1
print(round(math.pi, stepen(d)))
d = 0.0000000000001
print(round(math.pi, stepen(d)))
