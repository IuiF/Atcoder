from collections import defaultdict


n = int(input())
d = defaultdict(int)
for _ in range(n):
    d[input()] += 1
max_key = max(d, key=lambda x: d[x])
print(max_key)
