from collections import defaultdict


n, m = map(int, input().split())

s = [[] for _ in range(n + 1)]
for i in range(m):
    tmp = list(map(int, input().split()))
    for j in tmp[1:]:
        s[j].append(i + 1)

p = list(map(int, input().split()))
ans = 0

for i in range(2**n):
    sub = defaultdict(int)
    for j in range(n):
        if (i >> j) & 1:
            for k in s[j + 1]:
                sub[k] += 1
    flag = True
    for j in range(m):
        if sub[j + 1] % 2 != p[j]:
            flag = False
    if flag:
        ans += 1


print(ans)
