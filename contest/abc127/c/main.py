N, M = map(int, input().split())

L_max = 0
R_min = 10**5

for _ in range(M):
    tmp = list(map(int, input().split()))
    L_max = max(L_max, tmp[0])
    R_min = min(R_min, tmp[1])
if R_min - L_max < 0:
    print(0)
else:
    print(R_min - L_max + 1)
