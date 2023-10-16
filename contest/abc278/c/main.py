from collections import defaultdict


n, q = map(int, input().split())
d = defaultdict(bool)
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        d[f"{a}_{b}"] = True
    elif t == 2:
        d[f"{a}_{b}"] = False
    else:
        if d[f"{a}_{b}"] == True and d[f"{b}_{a}"] == True:
            print("Yes")
        else:
            print("No")
