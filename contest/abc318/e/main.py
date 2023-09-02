from collections import defaultdict
import itertools


N = int(input())
A = list(map(int, input().split()))
ans = 0
D = defaultdict(list)
for i in range(N):
    D[A[i]].append(i)

for k, v in D.items():
    if len(v) > 1:
        comb = list(itertools.combinations(v, 2))
        a, b = 10**10, 10**10
        tmp = 0

        for i, j in comb:
            if j > b:
                tmp += 1
            else:
                tmp = 0
            a = i
            b = j
            ans += j - i - 1
            ans -= tmp


print(ans)
