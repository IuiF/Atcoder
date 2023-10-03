from collections import defaultdict

n = int(input())
s = defaultdict(int)

for _ in range(n):
    s[input()] += 1

ans = max(s, key=lambda x: s[x])
print(ans)
