def find_monetka(x, y):
    if -1 > x_point or x_point > 1 or -1 > y_point or y_point > 1:
        print('Монетки в области нет')
    else:
        print('Монетка где-то рядом')


x_point = float(input('По горизонтали: '))
y_point = float(input('По вертикали: '))

find_monetka(x_point, y_point)
