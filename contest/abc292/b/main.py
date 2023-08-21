from collections import defaultdict


n, q = map(int, input().split())
p = defaultdict(int)
for _ in range(q):
    a, b = map(int, input().split())
    if a == 1:
        p[b] += 1
    elif a == 2:
        p[b] += 2
    else:
        if p[b] > 1:
            print("Yes")
        else:
            print("No")
