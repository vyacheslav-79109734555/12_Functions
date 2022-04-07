import math


def my_Distance(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print(distance)


def between_Distance(x_1, y_1, x_2, y_2):
    distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    print(distance)


print('Введите данные:\n1 - расстояние до точки; \n2 - расстояние между двумя точками;')

choice = int(input('Ввод: '))
if choice == 1:
    x = float(input('Введите координату "x": '))
    y = float(input('Введите координату "y": '))
    my_Distance(x, y)
elif choice == 2:
    x_1 = float(input('Введите координату "x" точки А: '))
    y_1 = float(input('Введите координату "y" точки А: '))
    x_2 = float(input('Введите координату "x" точки В: '))
    y_2 = float(input('Введите координату "y" точки В: '))
    between_Distance(x_1, y_1, x_2, y_2)
else:
    print('Ошибка ввода')
