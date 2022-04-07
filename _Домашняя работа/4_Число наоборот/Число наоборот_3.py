def backwards_numb(num):
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num //= 10
    print(f'Число наоборот: {result}')


while True:
    numb = int(input('Введите последовательность чисел: '))
    if numb == 0:
        print('Программа завершена!')
        break

    backwards_numb(numb)
