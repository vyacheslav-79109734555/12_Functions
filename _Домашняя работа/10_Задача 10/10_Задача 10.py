def quest():
    print(
        'Вы находитесь в квартире.\nзадача - покинуть ее!\nВ квартире есть три комнаты (спальня, кухня, '
        'ванна) и коридор.')
    a = str(input('Начнем?: '))
    if a == 'да' or 'Да' or 'ok':
        hallway()
    else:
        print('Игра окончена')


def bedroom():
    print('Вы в спальне. Куда идем?\n1 - в ванну\n2 - в коридор\n')
    i = int(input('Ввод: '))
    if i == 1:
        bath()
    elif i == 2:
        hallway()


def kitchen():
    print('Вы на кухне. Куда идем?\n1 - в коридор')
    i = int(input('Ввод: '))
    if i == 1:
        hallway()


def bath():
    print('Вы в ванне. Куда идем?\n1 - в коридор\n2 - в спальню\n')
    i = int(input('Ввод: '))
    if i == 1:
        hallway()
    elif i == 2:
        pass
        bedroom()


def hallway():
    print(
        'Вы в коридоре. Куда идем?\n'
        '1 - в спальню\n'
        '2 - в ванну\n'
        '3 - на кухню\n'
        '4 - в дверь\n'
    )
    i = int(input('Ввод: '))
    if i == 1:
        pass
        bedroom()
    elif i == 2:
        pass
        bath()
    elif i == 3:
        pass
        kitchen()
    elif i == 4:
        print('Вы вышли из квартиры!\n')
        quest()


quest()
hallway()
bath()
kitchen()
bedroom()

print('игра окончена!')
