n, x = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ans = float("inf")
t = 0
for i in range(n):
    a, b = ab[i]
    t += a + b
    if i == x:
        break
    ans = min(ans, t + b * (x - i - 1))

print(ans)
