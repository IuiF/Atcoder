n, q = map(int, input().split())
a = [0 for _ in range(n + 1)]
for _ in range(q):
    l, r, t = map(int, input().split())
    a[l : r + 1] = [t] * (r - l + 1)

for i in range(1, n + 1):
    print(a[i])
