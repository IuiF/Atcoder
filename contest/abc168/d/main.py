from collections import deque


n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

dist = [0] * (n)
queue = deque([0])

while queue:
    v = queue.popleft()
    for nv in g[v]:
        if dist[nv] == 0:
            dist[nv] = dist[v] + 1
            queue.append(nv)

if all(dist) >= 0:
    print("Yes")
    dist[0] = -1

for i in range(1, n):
    tmp = float("inf")
    t = -1
    for j in g[i]:
        tmp = min(tmp, dist[j])
        if tmp == dist[j]:
            t = j
    print(t + 1)

# print(dist)
