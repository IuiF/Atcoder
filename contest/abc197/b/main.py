h, w, x, y = map(int, input().split())
ans = 0
S = [list("*" for _ in range(w + 2)) for _ in range(h + 2)]

for i in range(h):
    tmp = list(input())
    for j in range(w):
        S[i + 1][j + 1] = tmp[j]

if S[x][y] == ".":
    ans += 1

    i = x + 1
    while S[i][y] != "*":
        if S[i][y] == ".":
            ans += 1
        elif S[i][y] == "#":
            break
        i += 1
    i = x - 1
    while S[i][y] != "*":
        if S[i][y] == ".":
            ans += 1
        elif S[i][y] == "#":
            break
        i -= 1
    i = y + 1
    while S[x][i] != "*":
        if S[x][i] == ".":
            ans += 1
        elif S[x][i] == "#":
            break
        i += 1
    i = y - 1
    while S[x][i] != "*":
        if S[x][i] == ".":
            ans += 1
        elif S[x][i] == "#":
            break
        i -= 1

print(ans)
