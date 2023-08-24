n, m = map(int, input().split())
WA = 0
AC = 0
flag = [False for _ in range(n)]
tWA = [0 for _ in range(n)]

for _ in range(m):
    a, b = input().split()
    a = int(a)
    if b == "WA" and flag[a - 1]:
        continue
    elif b == "AC" and flag[a - 1]:
        continue
    elif b == "WA" and not flag[a - 1]:
        tWA[a - 1] += 1
    elif b == "AC" and not flag[a - 1]:
        flag[a - 1] = True
        WA += tWA[a - 1]
        AC += 1

print(AC, WA)
