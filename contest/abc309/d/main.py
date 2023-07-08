from collections import deque


def bfs(G, s):
    dist = [-1] * len(G)
    queue = deque([s])
    dist[s] = 0

    while queue:
        v = queue.popleft()
        for u in G[v]:
            if dist[u] != -1:
                continue
            dist[u] = dist[v] + 1
            queue.append(u)
    return dist


N1, N2, M = map(int, input().split())
G = [[] for _ in range(N1 + N2 + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    if (1 <= a <= N1 and 1 <= b <= N1) or (
        N1 + 1 <= a <= N1 + N2 and N1 + 1 <= b <= N1 + N2
    ):
        G[a].append(b)
        G[b].append(a)

dist_1 = bfs(G, 1)
dist_2 = bfs(G, N1 + N2)

max_dist_1 = max(dist_1[1 : N1 + 1])
max_dist_2 = max(dist_2[N1 + 1 : N1 + N2 + 1])


print(max_dist_1 + max_dist_2 + 1)
