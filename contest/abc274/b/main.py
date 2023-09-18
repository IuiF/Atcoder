h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
ans = []
for i in range(w):
    tmp = 0
    for j in range(h):
        if c[j][i] == "#":
            tmp += 1
    ans.append(tmp)
print(*ans)
