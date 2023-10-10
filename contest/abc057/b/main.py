n, m = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
c = [list(map(int, input().split())) for _ in range(m)]
for i in range(n):
    tmp = float("inf")
    ans = -1
    for j in range(m):
        L = abs(p[i][0] - c[j][0]) + abs(p[i][1] - c[j][1])
        if L < tmp:
            tmp = L
            ans = j
    print(ans + 1)
