n, m = map(int, input().split())
a = list(map(int, input().split()))
p = 1
c = 0
while p <= n:
    while p <= a[c]:
        print(a[c] - p)
        p += 1
    c += 1
