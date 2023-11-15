from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)

for i in a:
    d[i] += 1

ans = 0
for k, v in d.items():
    for x, y in d.items():
        ans += (k - x) ** 2 * (v * y)

print(ans // 2)
