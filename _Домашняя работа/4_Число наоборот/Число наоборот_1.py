def number():
    numb = input('\nВведите последовательность чисел: ')
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
    print('Число наоборот: ', end='')
    n = 0
    for i in range(1, a + 1):
        if i != 0:
            result = numb % 10
            a = numb // 10
            numb = a
        print(result, end=' ')  # цифры на разных строках
    number()


def stop():
    print('Программа завершена!')


number()

