n, t = map(int, input().split())
ans = 10**5

for _ in range(n):
    a, b = map(int, input().split())
    if t >= b:
        ans = min(ans, a)

print(ans if ans != 10**5 else "TLE")
