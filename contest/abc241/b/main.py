from collections import defaultdict


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = defaultdict(int)

for i in a:
    d[i] += 1
for i in b:
    d[i] -= 1
    if d[i] < 0:
        print("No")
        exit()
print("Yes")
