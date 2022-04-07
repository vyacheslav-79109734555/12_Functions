def mainMenu():
    # приглашение ввода
    print('        Выбери игру:        \nесли: «Камень, ножницы, бумага» - ввод цифра - 1'
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
        # то вызываем функцию: guess_the_number()
        guess_the_number()
    # Если greeting любое значение
    else:
        print('Ошибка ввода, попробуй еще раз: \n')
        mainMenu()


def rock_paper_scissors():
    print('Раз, два, три, потрясли кулачки: твой ход, что у тебя?')
    print('если:\nКамень - ввод цифра - 1\nНожницы - ввод цифра - 2\nБумага - ввод цифра - 3')
    result = input('Ввод: ')
    if int(result) == 1:
        print('У тебя камень, а у меня бумага! Я ПОБЕДИЛ!\nИграем еще?\nесли: НЕТ ввод цифра - 0\n')
        rock_paper_scissors()
    elif int(result) == 2:
        print('У тебя ножницы, а у меня камень! Я ПОБЕДИЛ!\nИграем еще?\nесли: НЕТ ввод цифра - 0\n')
        rock_paper_scissors()
    elif int(result) == 3:
        print('У тебя бумага, а у меня ножницы! Я ПОБЕДИЛ!\nИграем еще?\nесли: НЕТ ввод цифра - 0\n')
        rock_paper_scissors()
    elif int(result) == 0:
        print('Игра окончена!\n')
        mainMenu()


def guess_the_number():
    print('Угадай! какое число загадали?: ')
    numb = input('Введи число? ')
    numbers = 10
    if numb.isdigit():
        numb = int(numb)
        if numb > numbers:
            print('Загаданное число меньше !\n')
            guess_the_number()
        elif numb < numbers:
            print('Загаданное число больше !\n')
            guess_the_number()
        else:
            print('Точно! загаданное число:', numb)
            mainMenu()


mainMenu()
