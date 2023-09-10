from copy import deepcopy


n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for _ in range(m)]

for p, x in px:
    tmp = deepcopy(t)
    tmp[p - 1] = x
    print(sum(tmp))
