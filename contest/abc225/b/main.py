from collections import defaultdict


d = defaultdict(int)
n = int(input())
for i in range(n - 1):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] += 1
f = False
for k, v in d.items():
    if v == n - 1:
        f = True
print("Yes" if f else "No")
