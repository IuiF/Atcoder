from typing import Counter


s = list(input())
t = Counter(s)

for i, j in t.items():
    if j == 1:
        print(s.index(i) + 1)
        exit()
