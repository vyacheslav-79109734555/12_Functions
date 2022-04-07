def test():
    n = int(input('Введите целое число: '))
    if n > 0:
        positive()
    elif n < 0:
        negative()
    else:
        print('Вы ввели " 0 "\n')
        test()


def positive():
    print('"Положительное"\n')
    test()


def negative():
    print('"Отрицательное"\n')
    test()


test()
