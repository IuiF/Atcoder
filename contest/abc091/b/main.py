from collections import defaultdict

n = int(input())
a = defaultdict(int)
b = defaultdict(int)
for i in range(n):
    a[input()] += 1
m = int(input())
for i in range(m):
    b[input()] += 1
ans = 0
for i, j in a.items():
    tmp = j
    tmp -= b[i]
    ans = max(ans, tmp)
print(ans)
