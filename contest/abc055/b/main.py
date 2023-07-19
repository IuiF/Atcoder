from math import factorial


N = int(input())

ans = factorial(N)
print(ans % (10**9 + 7))
