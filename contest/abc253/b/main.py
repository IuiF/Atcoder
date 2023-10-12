h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
b = []
for i in range(h):
    for j in range(w):
        if a[i][j] == "o":
            b.append((i, j))
print(abs(b[0][0] - b[1][0]) + abs(b[0][1] - b[1][1]))
