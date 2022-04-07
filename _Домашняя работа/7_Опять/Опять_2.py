def minimum(num_1, num_2):
    result = (numbers_1 + numbers_2 - abs(numbers_1 - numbers_2)) / 2
    print(f'минимальная цифра {int(result)}')


numbers_1 = int(input('Введите первое число: '))
numbers_2 = int(input('Введите второе число: '))

minimum(numbers_1, numbers_2)
