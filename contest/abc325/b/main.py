n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(24):
    t = 0
    for j, k in w:
        k -= i
        if k < 0:
            k += 24
        if 9 <= k <= 17:
            t += j
    ans = max(ans, t)

print(ans)
