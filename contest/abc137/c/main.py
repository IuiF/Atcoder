from collections import Counter, defaultdict


n = int(input())
ans = 0
dic = defaultdict(int)
for _ in range(n):
    s = list(input())
    s = Counter(s)
    s = str(sorted(s.items()))
    dic[s] += 1

for i in dic.values():
    ans += (i - 1) * (i) // 2

print(ans)
