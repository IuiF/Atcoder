import itertools


s, k = input().split()
s = list(s)
k = int(k)

ans = set(itertools.permutations(s))
ans = list(ans)
ans.sort()
print("".join(ans[k - 1]))
