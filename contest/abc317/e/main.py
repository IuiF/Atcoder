from collections import deque

h, w = map(int, input().split())
M = [list(input()) for _ in range(h)]
check = [[False for _ in range(w)] for _ in range(h)]
start, goal = None, None

for i in range(h):
    for j in range(w):
        if M[i][j] in ">":
            for k in range(j + 1, w):
                if M[i][k] in [">", "v", "<", "^", "#"]:
                    break
                check[i][k] = True
        elif M[i][j] == "<":
            for k in range(j - 1, -1, -1):
                if M[i][k] in [">", "v", "<", "^", "#"]:
                    break
                check[i][k] = True
        elif M[i][j] == "^":
            for k in range(i - 1, -1, -1):
                if M[k][j] in [">", "v", "<", "^", "#"]:
                    break
                check[k][j] = True
        elif M[i][j] == "v":
            for k in range(i + 1, h):
                if M[k][j] in [">", "v", "<", "^", "#"]:
                    break
                check[k][j] = True

for i in range(h):
    for j in range(w):
        if M[i][j] in [">", "v", "<", "^"] or check[i][j]:
            M[i][j] = "#"
        elif M[i][j] == "S":
            start = (i, j)
        elif M[i][j] == "G":
            goal = (i, j)

visited = [[False for _ in range(w)] for _ in range(h)]
queue = deque([(start, 0)])
ans = 0
dist = 0

while queue:
    (i, j), dist = queue.popleft()
    if (i, j) == goal:
        ans = dist
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and M[ni][nj] != "#":
            visited[ni][nj] = True
            queue.append(((ni, nj), dist + 1))
if ans == 0:
    print(-1)
else:
    print(ans)
