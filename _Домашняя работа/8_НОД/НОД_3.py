
# если например: несколько чисел 14 35 28 91
# Наибольший общий делитель: 7
def nod(num):
    a = num[0]
    for j in range(len(num)):
        b = num[j]
        while b:
            a, b = b, a % b
    return a


n = input('Введите числа через " пробел ": ').split()
x = []
for i in n:
    x.append(int(i))

print(f'Наибольший общий делитель: {nod(x)}')
