n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        tmp = ((x[i][0] - x[j][0]) ** 2 + (x[i][1] - x[j][1]) ** 2) ** (1 / 2)
        ans = max(ans, tmp)
print(ans)
