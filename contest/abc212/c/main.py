n, m = map(int, input().split())
a = list(set(map(int, input().split())))
b = list(set(map(int, input().split())))
c = [(i, "a") for i in a] + [(i, "b") for i in b]
c.sort()
ans = float("inf")
for i in range(1, len(c)):
    if c[i][1] == c[i - 1][1]:
        continue
    t = abs(c[i - 1][0] - c[i][0])
    ans = min(ans, t)
print(ans)
