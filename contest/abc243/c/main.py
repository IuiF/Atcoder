from collections import defaultdict


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
s = list(input())
b = [(a[i][0], a[i][1], s[i]) for i in range(n)]
c = defaultdict(list)
for i in range(n):
    c[b[i][1]].append((b[i][0], b[i][2]))

for i in c.values():
    max_L, min_R = 0, 10**10
    for j in i:
        if j[1] == "R":
            min_R = min(min_R, j[0])
        else:
            max_L = max(max_L, j[0])
    if min_R < max_L:
        print("Yes")
        exit()
print("No")
