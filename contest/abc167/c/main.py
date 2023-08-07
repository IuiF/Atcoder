n, m, x = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(n)]
ans = 10**10

for i in range(2**n):  # bit全探索
    sub = [0 for _ in range(m + 1)]
    for j in range(n):
        if (i >> j) & 1:
            for k in range(m + 1):
                sub[k] += CA[j][k]
    flag = True
    for j in range(1, m + 1):
        if sub[j] < x:
            flag = False
            break
    if flag:
        ans = min(ans, sub[0])

print(ans if ans != 10**10 else -1)
