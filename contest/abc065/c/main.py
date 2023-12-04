import sys


sys.setrecursionlimit(10**6)


def factorial(n):
    MOD = 10**9 + 7
    if n == 0:
        return 1
    else:
        a = (n * factorial(n - 1)) % MOD
        return a


MOD = 10**9 + 7
n, m = map(int, input().split())
if abs(n - m) > 1:
    print(0)
elif abs(n - m) == 1:
    print((factorial(n) * factorial(m)) % MOD)
else:
    print((factorial(n) * factorial(m) * 2) % MOD)
