def greeting():
    print('Привет!')
    print('Добро пожаловать!')


while True:
    a = input('Зайдёте? Да/Нет: ')
    if a == 'Да' or a == 'да':
        greeting()
    else:
        print('Следующий!\n')
