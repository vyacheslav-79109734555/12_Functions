import math

a = float(input('Введите значения a = '))
b = float(input('Введите значения b = '))
i = (a + b + abs(a - b)) / 2
print('Наибольшее число:', int(i))
print('////////////////////////////////')
print('Наибольшее число используя функцию max():', int(max(a, b)))
