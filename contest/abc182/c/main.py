from collections import defaultdict


N = list(input())
t = sum(int(i) for i in N)
dc = defaultdict(int)
for i in N:
    i = int(i)
    i %= 3
    dc[i] += 1

if t % 3 == 0:
    print(0)
elif t % 3 == 1:
    if dc[1] > 0 and len(N) != 1:
        print(1)
    elif len(N) == 2:
        print(-1)
    elif dc[2] > 1:
        print(2)
    else:
        print(-1)
else:
    if dc[2] > 0 and len(N) != 1:
        print(1)
    elif len(N) == 2:
        print(-1)
    elif dc[1] > 1:
        print(2)
    else:
        print(-1)
