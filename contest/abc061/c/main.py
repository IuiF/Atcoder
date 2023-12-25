from collections import defaultdict


n, k = map(int, input().split())
dic = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    dic[a] += b
c = sorted(dic.items())

for i, j in c:
    k -= j
    if k <= 0:
        print(i)
        exit()
