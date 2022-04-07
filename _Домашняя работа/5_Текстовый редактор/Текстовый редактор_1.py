def count_letters():
    text = input('Введите текст: ')
    x = len(text)
    if x > 2:
        count_K(text)
        count_N(text)


def count_K(text):
    num = input('Какую цифру ищем?_')
    counter_symbol_n = 0
    for symbol in text:
        if symbol == num:
            counter_symbol_n += 1
    print('Количество цифр', num, ':', counter_symbol_n)


def count_N(text):
    symb = input('Какую букву ищем?_')
    counter_symbol_s = 0
    for symbol in text:
        if symbol == symb:
            counter_symbol_s += 1
    print('Количество букв', symb, ':', counter_symbol_s)


count_letters()
