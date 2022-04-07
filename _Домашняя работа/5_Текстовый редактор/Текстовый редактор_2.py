def count_letters(txt, num, symb):
    n = 0
    s = 0
    for letter in txt:
        if letter == num:
            n += 1
        elif letter.lower() == symb.lower():
            s += 1
    print(f'Количество цифр {number}: {n}', f'Количество букв {symbol}: {s}', sep='\n')


text = input('Введите текст: ')
number = input('Какую цифру ищем?_')
symbol = input('Какую букву ищем?_')

count_letters(text, number, symbol)
