from collections import Counter


n = int(input())
a = list(map(int, input().split()))
b = Counter(a)
c = sorted(b.items(), key=lambda x: x[0])
t = sum(a)

dic = {}
for i, j in c:
    t -= i * j
    dic[i] = t

ans = []
for i in a:
    ans.append(dic[i])

print(*ans)
