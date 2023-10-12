N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        x, y = a[i][0], a[i][1]
        w, z = a[j][0], a[j][1]
        if 1 >= (z - y) / (x - w) >= -1:
            ans += 1
print(ans)
