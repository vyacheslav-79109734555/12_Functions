def positive():
    print('"Положительное"\n')
    test()


def negative():
    print('"Отрицательное"\n')
    test()


def test():
    n = int(input('Введите целое число: '))
    if n > 0:
        positive()
    elif n < 0:
        negative()
    else:
        print('Вы ввели " 0 "\n')
        test()


test()
