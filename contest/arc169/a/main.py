from collections import deque

n = int(input())
a = list(map(int, input().split()))
p = list(map(int, input().split()))
G = [[] for _ in range(n)]

for i in range(1, n):
    G[p[i - 1] - 1].append(i)

visited = [False] * n
queue = deque([0])
leaf_nodes = []

while queue:
    node = queue.popleft()
    visited[node] = True

    if not G[node]:
        leaf_nodes.append(node)

    for child in G[node]:
        if not visited[child]:
            queue.append(child)

S = sum(a[i] for i in leaf_nodes)


if S > 0:
    print("+")
elif S < 0:
    print("-")
else:
    t = sum(a[i] for i in range(n) if visited[i])
    if t == 0:
        print("0")
    elif t > 0:
        print("+")
    else:
        print("-")
