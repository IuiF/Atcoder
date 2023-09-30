### TLE


n, k, p = map(int, input().split())
C = []
A = []

for _ in range(n):
    a, *b = map(int, input().split())
    C.append(a)
    A.append(b)
kp = [0 for _ in range(k)]
for i in A:
    for j in range(k):
        kp[j] += i[j]

if min(kp) < p:
    print(-1)
    exit()
else:
    for i in range(k):
        kp[i] = kp[i] - p

sub = []
for i in range(n):
    flag = True
    for j in range(k):
        if A[i][j] > kp[j]:
            flag = False
    if flag:
        sub.append((C[i], A[i]))

ans = 0
for i in range(2 ** len(sub)):
    sub0 = []
    sub1 = [0 for _ in range(k)]
    for j in range(len(sub)):
        if (i >> j) & 1:
            tmp1, tmp2 = sub[j]
            sub0.append(tmp1)
            for kk in range(k):
                sub1[kk] += tmp2[kk]
    if all(sub1[j] <= kp[j] for j in range(k)):
        ans = max(ans, sum(sub0))


print(sum(C) - ans)
