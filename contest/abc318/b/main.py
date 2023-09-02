n = int(input())
F = [[False for _ in range(100)] for _ in range(100)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    if a == b or c == d:
        continue
    for i in range(a, b):
        for j in range(c, d):
            F[i][j] = True

ans = 0
for i in range(100):
    for j in range(100):
        if F[i][j]:
            ans += 1

print(ans)
