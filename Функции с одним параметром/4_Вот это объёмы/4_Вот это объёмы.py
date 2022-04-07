import math


def sphereArea(r):
    print('площадь сферы =', 4 * math.pi * r ** 2)


def sphereVolume(r):
    print('объём шара =', 3 / 4 * math.pi * r ** 3)


r = float(input('Введите радиус планеты: '))
sphereArea(r)
sphereVolume(r)
