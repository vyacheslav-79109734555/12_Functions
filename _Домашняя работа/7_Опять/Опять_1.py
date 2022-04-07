def minimum():
    numbers_1 = int(input('Введите первое число: '))
    numbers_2 = int(input('Введите второе число: '))

    result = (numbers_1 + numbers_2 + abs(numbers_1 - numbers_2)) / 2
    if result == numbers_1:
        print('минимальная цифра', numbers_2)
        minimum()
    elif result == numbers_2:
        print('минимальная цифра', numbers_1)
        minimum()


minimum()
