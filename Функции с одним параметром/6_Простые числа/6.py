def isPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


n = int(input())
if isPrime(n):
    print('YES')
else:
    print('NO')