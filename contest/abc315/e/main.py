import sys

sys.setrecursionlimit(10**7)


def dfs(v):
    global ans, visited
    if v in visited:
        return
    visited.add(v)
    for i in P[v]:
        dfs(i)
    if v != 1:
        ans.append(v)


N = int(input())
visited = set()

P = [[]]
for _ in range(N):
    C, *D = map(int, input().split())
    P.append(D)

ans = []
dfs(1)

print(*ans)
