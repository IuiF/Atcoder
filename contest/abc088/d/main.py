from collections import deque


h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
arr = [[-1 for _ in range(w)] for _ in range(h)]
queue = deque([((0, 0), 0)])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    v, d = queue.popleft()
    if v[0] == h - 1 and v[1] == w - 1:
        break

    for i, j in zip(dx, dy):
        nx, ny = v[0] + i, v[1] + j
        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == "." and arr[nx][ny] == -1:
            arr[nx][ny] = d + 1
            queue.append(((nx, ny), d + 1))


if arr[-1][-1] == -1:
    print(-1)
else:
    sh = sum(s[i].count("#") for i in range(h))
    print(h * w - arr[-1][-1] - sh - 1)
