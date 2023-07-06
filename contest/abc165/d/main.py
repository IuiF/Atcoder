a, b, n = map(int, input().split())

if b > n:
    print(int(a * n / b))
else:
    print(int(a * (b - 1) / b))
