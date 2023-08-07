from copy import deepcopy


H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]
ans = 0

for i in range(2**H):
    for j in range(2**W):
        sub = deepcopy(C)
        for k in range(H):
            if (i >> k) & 1:
                sub[k] = ["." for _ in range(W)]
        for l in range(W):
            if (j >> l) & 1:
                for x in range(H):
                    sub[x][l] = "."

        tmp = 0
        for y in range(H):
            tmp += sub[y].count("#")
        if tmp == K:
            ans += 1

print(ans)
