def dfs(v, depth):
    global ans
    if depth == N - 1:
        ans += 1
        return
    visited[v] = True

    for i in G[v]:
        if not visited[i]:
            dfs(i, depth + 1)
            visited[i] = False


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

ans = 0
visited = [False] * N
dfs(0, 0)

print(ans)
