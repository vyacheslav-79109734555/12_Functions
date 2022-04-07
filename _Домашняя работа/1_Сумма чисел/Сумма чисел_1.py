def summa_n():
    numb = input('Введите целое, положительное число N: ')
    if numb.isdigit():
        counter(numb)
    else:
        print('Ошибка ввода! попробуйте еще раз: ')
        summa_n()


def counter(numb):
    count = 0
    n = int(numb)

    for i in range(1, n + 1):
        count += i
    print('сумму всех чисел =', count)
    summa_n()


summa_n()
