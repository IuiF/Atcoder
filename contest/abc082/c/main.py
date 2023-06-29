import collections


N = int(input())
arr = list(map(int, input().split()))
d = collections.Counter(arr)
ans = 0

for k, v in d.items():
    if k <= v:
        ans += v - k
    else:
        ans += v

print(ans)
