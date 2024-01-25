n, m = map(int, input().split())
if n == m == 1:
    print(1)
elif m == 1:
    print(max(0, n - 2))
elif n == 1:
    print(max(0, m - 2))
elif m == 2 or n == 2:
    print(0)
else:
    print(m * n - n * 2 - (m - 2) * 2)
