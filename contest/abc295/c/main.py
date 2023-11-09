from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)
for i in a:
    d[i] += 1
ans = 0
for k, v in d.items():
    ans += v // 2

print(ans)
