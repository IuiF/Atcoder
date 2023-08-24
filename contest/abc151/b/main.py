n, k, m = map(int, input().split())
a = sum(map(int, input().split()))
if a / n >= m:
    print(0)
elif (a + k) / n >= m:
    print(n * m - a)
else:
    print(-1)
