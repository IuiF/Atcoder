n, d = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(i + 1, n):
        tmp = 0
        for k in range(d):
            tmp += (X[i][k] - X[j][k]) ** 2
        tmp = tmp**0.5
        if tmp == int(tmp):
            ans += 1

print(ans)
