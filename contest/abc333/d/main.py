import sys

sys.setrecursionlimit(10**6)


def dfs_count_subtree_sizes(G, vertex, parent, subtree_sizes):
    subtree_size = 1
    for child in G[vertex]:
        if child != parent:
            subtree_size += dfs_count_subtree_sizes(G, child, vertex, subtree_sizes)
    subtree_sizes[vertex] = subtree_size
    return subtree_size


def solve(G, n):
    subtree_sizes = [0] * n
    dfs_count_subtree_sizes(G, 0, -1, subtree_sizes)
    return n - max(subtree_sizes[child] for child in G[0])


n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    G[x].append(y)
    G[y].append(x)

if len(G[0]) == 1:
    print(1)
else:
    print(solve(G, n))
