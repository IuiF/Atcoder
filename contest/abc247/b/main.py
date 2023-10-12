from collections import defaultdict

n = int(input())
ar = [list(input().split()) for _ in range(n)]

d = defaultdict(int)

for i in range(n):
    a, b = ar[i]
    d[a] += 1
    d[b] += 1
for i in range(n):
    a, b = ar[i]
    if d[a] == 1 or d[b] == 1 or (a == b and d[a] == 2 and d[b] == 2):
        continue
    else:
        print("No")
        exit()
print("Yes")
