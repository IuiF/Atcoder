n = int(input())
a = [[] for _ in range(n)]

for i in range(n):
    tmp = int(input())
    for j in range(tmp):
        x, y = map(int, input().split())
        a[i].append((x, y))

ans = 0
for i in range(2**n):
    sub = []
    flag = True
    for j in range(n):
        sub.append((i >> j) & 1)

    for j in range(n):
        if (i >> j) & 1:
            for k in a[j]:
                if sub[k[0] - 1] != k[1]:
                    flag = False
                    break

    if flag:
        ans = max(ans, sub.count(1))

print(ans)
