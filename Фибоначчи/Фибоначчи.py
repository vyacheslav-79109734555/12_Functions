def fib(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


print(fib(int(input('Введите целое неотрицательное число: '))))
