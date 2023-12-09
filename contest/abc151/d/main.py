from collections import deque


def bfs(sx, sy):
    dist = [[-1] * w for _ in range(h)]
    dist[sx][sy] = 0
    queue = deque([(sx, sy)])
    max_dist = 0
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < h and 0 <= ny < w and M[nx][ny] != "#" and dist[nx][ny] == -1:
                queue.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                max_dist = max(max_dist, dist[nx][ny])
    return max_dist


h, w = map(int, input().split())
M = [list(input()) for _ in range(h)]
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for i in range(h):
    for j in range(w):
        if M[i][j] == ".":
            ans = max(ans, bfs(i, j))

print(ans)
