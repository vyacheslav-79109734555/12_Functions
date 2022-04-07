def nod(a, b):
    b, a = sorted((a, b))
    while b:
        a, b = b, a % b
    return a


first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

print(f'Наибольший общий делитель: {nod(first_num, second_num)}')

