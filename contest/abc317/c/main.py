import sys

sys.setrecursionlimit(10**6)


def dfs(v):
    global visited, G
    visited.add(v)
    max_dist = 0
    for i, j in G[v]:
        if i not in visited:
            max_dist = max(max_dist, j + dfs(i))
    visited.remove(v)
    return max_dist


n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a - 1].append((b - 1, c))
    G[b - 1].append((a - 1, c))

visited = set()
ans = 0
for i in range(n):
    visited.clear()
    ans = max(ans, dfs(i))

print(ans)
