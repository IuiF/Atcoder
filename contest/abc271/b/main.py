n, q = map(int, input().split())
ar = [list(map(int, input().split())) for _ in range(n)]
for _ in range(q):
    a, b = map(int, input().split())
    print(ar[a - 1][b])
