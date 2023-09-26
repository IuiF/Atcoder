import itertools
import math

N = int(input())
L = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

ans = []
ans_len = []

for i in range(1, 11):
    ans_len.append(math.comb(10, i))

for i in range(1, 11):
    N -= ans_len[i - 1]
    if N < 0:
        N += ans_len[i - 1]
        tmp = list(itertools.combinations(L, i))
        for j in tmp:
            j = j[::-1]
            t = "".join(j)
            ans.append(t)
        ans.sort()
        break

print(ans[N])
