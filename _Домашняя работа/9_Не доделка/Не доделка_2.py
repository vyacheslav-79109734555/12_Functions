import random


def rock_paper_scissors():
    print('Раз, два, три, потрясли кулачки: твой ход, что у тебя?')
    print('если:\nКамень - ввод - 1\nНожницы - ввод - 2\nБумага - ввод - 3')
    a = int(input('Первый игрок, твой ход: '))
    b = int(input('Второй игрок, твой ход: '))
    if (a == 1 and b == 2) or (a == 2 and b == 1):
        if a == 1:
            txt = 'Первый игрок'
        else:
            txt = 'Второй игрок'
        print(
            f'Первый игрок выбрал {1} \nВторой игрок выбрал {2} '
            f'\nКамень бъет ножницы! {txt} победил \nИграем еще?\nесли: НЕТ ввод цифра - 0\n')
    if (a == 2 and b == 3) or (a == 3 and b == 2):
        if a == 2:
            txt = 'Первый игрок'
        else:
            txt = 'Второй игрок'
        print(
            f'Первый игрок выбрал {2} \nВторой игрок выбрал {3} '
            f'\nНожницы бъет Бумагу! {txt} победил \nИграем еще?\nесли: НЕТ ввод цифра - 0\n')
    if (a == 3 and b == 1) or (a == 1 and b == 3):
        if a == 3:
            txt = 'Первый игрок'
        else:
            txt = 'Второй игрок'
        print(
            f'Первый игрок выбрал {3} \nВторой игрок выбрал {1} '
            f'\nБумага кроет Камень! {txt} победил \nИграем еще?\nесли: НЕТ ввод цифра - 0\n')
    elif a == 0 or b == 0:
        print('Игра окончена!\n')
    mainMenu()


def guess_the_number(numbers):
    print('Угадай! какое число я загадал?: ')
    while True:
        numb = input('Введи число? ')
        if numb.isdigit():
            numb = int(numb)
            if int(numb) == 100:
                print('Игра окончена!')
                break
            elif numb > numbers:
                print('Загаданное число *** Меньше !\n')
                guess_the_number(numbers)
            elif numb < numbers:
                print('Загаданное число *** Больше !\n')
                guess_the_number(numbers)
            else:
                print('Точно! загаданное число:', numb)

        mainMenu()


def mainMenu():
    # приглашение ввода
    print('\n        Выбери игру:        \nесли: «Камень, ножницы, бумага» - ввод цифра - 1'
          '\nесли: «Угадай число» - ввод цифра - 2')
    # переменная приветствие
    greeting = input('Ввод: ')
    if greeting.isdigit():
        greeting = int(greeting)
    else:
        print('Ошибка ввода, попробуй еще раз: \n')
        mainMenu()
    # Если greeting целое число и равно 1
    if greeting == 1:
        # то вызываем функцию: rock_paper_scissors()
        rock_paper_scissors()
    # Если greeting целое число и равно 2
    elif int(greeting) == 2:
        print('Для выхода из игры введите 100.')
        print('*******************************')
        # то вызываем функцию: guess_the_number()
        guess_the_number(random.randint(1, 100))
    # Если greeting любое значение
    else:
        print('Ошибка ввода, попробуй еще раз: \n')
        mainMenu()


mainMenu()
