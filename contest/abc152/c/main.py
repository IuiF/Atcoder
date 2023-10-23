n = int(input())
p = list(map(int, input().split()))
ans = 1
t = p[0]
for i in range(1, n):
    if t >= p[i]:
        ans += 1
    t = min(t, p[i])


print(ans)
