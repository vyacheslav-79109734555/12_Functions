def summa_n(n):
    count = 0
    for num in range(1, n + 1):
        count += num
    print(f'Сумму всех чисел от 1 до {n} = {count}')


numb = int(input('Введите целое, положительное число N: '))
if numb > 0:
    summa_n(numb)
else:
    print('Ошибка ввода! попробуйте еще раз: ')
