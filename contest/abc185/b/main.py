n, m, t = map(int, input().split())
p = 0
r = n
for _ in range(m):
    a, b = map(int, input().split())
    n -= a - p
    if n <= 0:
        print("No")
        exit()
    n += b - a
    if n > r:
        n = r
    p = b
if n - (t - p) <= 0:
    print("No")
else:
    print("Yes")
