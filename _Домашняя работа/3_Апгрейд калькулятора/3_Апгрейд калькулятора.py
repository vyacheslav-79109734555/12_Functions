def calculator():
    numbers_1 = input('Введите первое число: ')
    if numbers_1.isdigit():
        numbers_1 = float(numbers_1)
    else:
        print('Ошибка ввода! попробуйте еще раз: ')
        calculator()
    numbers_2 = input('Введите второе число: ')
    if numbers_2.isdigit():
        numbers_2 = float(numbers_2)
    else:
        print('Ошибка ввода! попробуйте еще раз: ')
        calculator()
    action = input('Какое действие выполнить из возможных:\n"+" "-" "*" "/" "**" "больше >" "< меньше"\n')

    if action == '+':
        addition(numbers_1, numbers_2)
    elif action == '-':
        subtraction(numbers_1, numbers_2)
    elif action == '*':
        multiply(numbers_1, numbers_2)
    elif action == '/':
        dividing(numbers_1, numbers_2)
    elif action == '**':
        exponentiation(numbers_1, numbers_2)
    elif action == '>':
        more(numbers_1, numbers_2)
    elif action == '<':
        less(numbers_1, numbers_2)
    elif action == '...':
        print('Вычисление закончено')


def addition(numbers_1, numbers_2):
    result = numbers_1 + numbers_2
    print(numbers_1, '+', numbers_2, '=', result)
    calculator()


def subtraction(numbers_1, numbers_2):
    result = numbers_1 - numbers_2
    print(numbers_1, '-', numbers_2, '=', result)
    calculator()


def multiply(numbers_1, numbers_2):
    result = numbers_1 * numbers_2
    print(numbers_1, '*', numbers_2, '=', result)
    calculator()


def dividing(numbers_1, numbers_2):
    result = numbers_1 / numbers_2
    print(numbers_1, '/', numbers_2, '=', result)
    calculator()


def exponentiation(numbers_1, numbers_2):
    result = numbers_1 ** numbers_2
    print(numbers_1, '**', numbers_2, '=', result)
    calculator()


def more(numbers_1, numbers_2):
    result = (numbers_1 + numbers_2 + abs(numbers_1 - numbers_2)) / 2
    print('максимальная цифра', result)
    calculator()


def less(numbers_1, numbers_2):
    result = (numbers_1 + numbers_2 + abs(numbers_1 - numbers_2)) / 2
    if result == numbers_1:
        print('минимальная цифра', numbers_2)
    elif result == numbers_2:
        print('минимальная цифра', numbers_1)
    calculator()


calculator()
