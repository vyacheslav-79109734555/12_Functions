def reverse():
    x = int(input('Введите последовательность целых чисел  заканчивающаяся числом 0: '))
    if x != 0:
        reverse()
        print(x)


reverse()
