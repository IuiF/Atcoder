N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = -(10**10)
for i in range(1, 2**10):
    sub = [0 for _ in range(N)]
    for j in range(10):
        if (i >> j) & 1 == 1:
            for k in range(N):
                if F[k][j] == 1:
                    sub[k] += 1

    tmp = 0
    for j in range(N):
        tmp += P[j][sub[j]]

    ans = max(ans, tmp)

print(ans)
