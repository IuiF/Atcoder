h, w = map(int, input().split())
S = []


S.append(["." for _ in range(w + 2)])
for _ in range(h):
    S.append(list("." + input() + "."))
S.append(["." for _ in range(w + 2)])

for i in range(1, h + 1):
    tmp = []
    for j in range(1, w + 1):
        if S[i][j] == "#":
            tmp.append("#")
        else:
            count = 0
            for k, l in [
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j - 1),
                (i, j),
                (i, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1),
            ]:
                if S[k][l] == "#":
                    count += 1
            tmp.append(count)
    print(*tmp, sep="")
