import sympy

counter_numb = int(input('Введите количество чисел в последовальности: '))
a = 0
b = 0
for i in range(counter_numb):
    print('Введите', i + 1, '- е число: ', end='')
    x = int(input())
    if sympy.isprime(x) == True:
        a += 1
    else:
        b += 1
print('простых чисел', a)
print('составных чисел', b)
