from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)

for i in a:
    d[i] += 1

for k, v in d.items():
    if v == 3:
        print(k)
        break
