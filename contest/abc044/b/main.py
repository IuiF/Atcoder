from collections import defaultdict


a = defaultdict(int)
w = input()
for i in range(len(w)):
    a[w[i]] += 1
for i, j in a.items():
    if j % 2 == 1:
        print("No")
        exit()
print("Yes")
