n = int(input())
d = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    t = d[i - 1]
    for j in range(1, t + 1):
        tmp = []
        for k in str(i):
            tmp.append(k)
        for k in str(j):
            tmp.append(k)
        if len(set(tmp)) == 1:
            ans += 1

print(ans)
