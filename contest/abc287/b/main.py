n, m = map(int, input().split())
S = list(input() for _ in range(n))
T = set(list(input() for _ in range(m)))
ans = 0
for i in S:
    if i[3:] in T:
        ans += 1

print(ans)
