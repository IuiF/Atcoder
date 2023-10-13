h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
f = False
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
c = list("snuke")

for i in range(h):
    for j in range(w):
        for k in range(8):
            x, y = i, j
            tmp = [[x + 1, y + 1]]
            tmp_s = [s[x][y]]
            for p in range(1, 5):
                x += dx[k]
                y += dy[k]
                if x < 0 or x >= h or y < 0 or y >= w:
                    break
                else:
                    tmp_s.append(s[x][y])
                    tmp.append([x + 1, y + 1])
            if tmp_s == c:
                for i in tmp:
                    print(*i)
                exit()
