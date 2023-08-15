n, a, b, c = map(int, input().split())
L = list(int(input()) for _ in range(n))
ans = float("inf")

for i in range(4**n):
    sub = [0, 0, 0]
    tmp = 0
    for j in range(n):
        if (i >> 2 * j) & 1:
            if ((i >> 2 * j) >> 1) & 1:
                if sub[0] != 0:
                    tmp += 10
                sub[0] += L[j]
            else:
                if sub[1] != 0:
                    tmp += 10
                sub[1] += L[j]
        else:
            if ((i >> 2 * j) >> 1) & 1:
                if sub[2] != 0:
                    tmp += 10
                sub[2] += L[j]
    if sub[0] == 0 or sub[1] == 0 or sub[2] == 0:
        continue
    tmp += abs(a - sub[0]) + abs(b - sub[1]) + abs(c - sub[2])
    ans = min(ans, tmp)

print(ans)
