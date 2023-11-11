from itertools import combinations


def tree_check(n, se):
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x
            return True
        return False

    for u, v, _ in se:
        if not union(u, v):
            return False

    return True


def solve(n, m, k, G):
    edges = []
    for u in range(n):
        for v, w in G[u]:
            if u < v:
                edges.append((u, v, w))

    ans = float("inf")

    for se in combinations(edges, n - 1):
        if tree_check(n, se):
            cost = sum(weight for _, _, weight in se) % k
            ans = min(ans, cost)

    return ans if ans != float("inf") else -1


n, m, k = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    G[u - 1].append((v - 1, w))
    G[v - 1].append((u - 1, w))

ans = solve(n, m, k, G)
print(ans)
