from collections import Counter


s = list(input())
c = Counter(s)
c = list(c.items())
c.sort(key=lambda x: (-x[1], x[0]))

print(c[0][0])
