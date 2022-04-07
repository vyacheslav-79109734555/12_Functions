def main_Menu():
    print('Ваш выбор:')
    print('1 - сделать что то хорошее')
    print('2 - сделать что то плохое')
    choice = int(input('Ввод действия: '))

    if choice == 1:
        good()
    elif choice == 2:
        bad()
    else:
        print('Ошибка ввода: введите 1 или 2')
        main_Menu()


def good():
    input('Нажмите ввод что бы вернуться в меню\n')
    print('Всё хорошо')
    main_Menu()


def bad():
    print('*********')
    print('Всё плохо\n')
    main_Menu()


main_Menu()
