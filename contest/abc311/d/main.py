from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

que = deque([(1, 1)])
visited[1][1] = True

while que:
    x, y = que.popleft()

    for i in range(4):
        nx, ny = x, y
        while True:
            if A[nx + dx[i]][ny + dy[i]] == "#":
                if not visited[nx][ny]:
                    que.append((nx, ny))  # type: ignore
                visited[nx][ny] = True
                break
            visited[nx][ny] = True
            nx += dx[i]
            ny += dy[i]

ans = 0
for row in visited:
    for i in row:
        if i:
            ans += 1


print(ans)
