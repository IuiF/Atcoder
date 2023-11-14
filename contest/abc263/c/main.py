import itertools


n, m = map(int, input().split())
arr = [i for i in range(1, m + 1)]
ans = list(itertools.combinations(arr, n))
ans.sort()

for i in ans:
    print(*i)
