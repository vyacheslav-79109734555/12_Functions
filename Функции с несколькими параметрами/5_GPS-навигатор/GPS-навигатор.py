import math


def distance_to_the_object(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print('расстояние до обьекта:', round(distance, 3))


def distance_a_b(x_1, y_1, x_2, y_2):
    distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    print('расстояние от точки А до точки В:', round(distance, 3))


print('Введите:\n1 - расстояние от себя до обьекта;\n2 - расстояние от точки А до точки В;')
choice = int(input('ввод: '))
if choice == 1:
    x = float(input('Введите координату "x": '))
    y = float(input('Введите координату "y": '))
    distance_to_the_object(x, y)
elif choice == 2:
    x_1 = float(input('Введите координату "x": '))
    y_1 = float(input('Введите координату "y": '))
    x_2 = float(input('Введите координату "x": '))
    y_2 = float(input('Введите координату "y": '))
    distance_a_b(x_1, y_1, x_2, y_2)
else:
    print('Ошибка ввода')
