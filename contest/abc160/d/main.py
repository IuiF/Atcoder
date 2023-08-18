from collections import deque


def bfs(start):
    queue = deque([start])
    dis = [-1] * n
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if dis[i] == -1:
                dis[i] = dis[v] + 1
                queue.append(i)
    return dis


n, x, y = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(n - 1):
    g[i].append(i + 1)
    g[i + 1].append(i)
g[x - 1].append(y - 1)
g[y - 1].append(x - 1)

count = [0] * n
for i in range(n):
    distances = bfs(i)
    for j in range(i + 1, n):
        count[distances[j]] += 1

for i in range(n - 1):
    print(count[i])
