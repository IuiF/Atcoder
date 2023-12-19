N, T = map(int, input().split())
t = list(map(int, input().split()))
ans = T
p = t[0] + T
for i in range(1, N):
    if p < t[i]:
        ans += T
        p = t[i] + T
    else:
        ans += T - (p - t[i])
        p = t[i] + T

print(ans)
