from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
D = defaultdict(int)

count = 0
for i in A:
    if D[i] == 1:
        count += 1
    else:
        D[i] += 1


if count % 2 == 0:
    print(len(D))
else:
    print(len(D) - 1)

# print(D)
