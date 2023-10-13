n, m = map(int, input().split())
f = [False for _ in range(n)]
a = list(map(int, input().split()))
for i in a:
    f[i - 1] = True

ans = []
i = 0
while i < n:
    if not f[i]:
        ans.append(i + 1)
        i += 1
    else:
        tmp = []
        p = i
        while p < n and f[p]:
            tmp.append(p + 1)
            p += 1
        tmp.append(p + 1)
        i = p + 1
        ans.extend(tmp[::-1])

print(*ans)
