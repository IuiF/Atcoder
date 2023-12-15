n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
if m == 1 or m - n < 0:
    print(0)
else:
    y = [abs(x[i] - x[i - 1]) for i in range(1, m)]
    y.sort()
    print(sum(y[: m - n]))
