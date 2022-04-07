def number():
    numb = input('Введите последовательность чисел: ')
    quantity = len(numb)
    if int(numb) == 0 and numb.isdigit():
        stop()
    elif numb.isdigit() > 0:
        a = int(quantity)
        numb = int(numb)
        backwards_numb(numb, a)
    else:
        print('Ошибка ввода! попробуйте еще раз: ')
        number()


def backwards_numb(numb, a):
    n = 0
    for i in range(1, a + 1):
        result = numb % 10
        numb = numb // 10
        n = n * 10
        n = n + result
    print(f'Число наоборот: {n} ')
    number()


def stop():
    print('Программа завершена!')


number()

