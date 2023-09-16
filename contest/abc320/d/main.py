from collections import defaultdict, deque

n, m = map(int, input().split())
ans = {i: None for i in range(1, n + 1)}
G = defaultdict(list)

for _ in range(m):
    a, b, x, y = map(int, input().split())
    G[a].append((b, x, y))
    G[b].append((a, -x, -y))

queue = deque([(1, 0, 0)])
visited = set()

while queue:
    node, x, y = queue.popleft()
    if node in visited:
        continue
    visited.add(node)

    ans[node] = (x, y)

    for next, dx, dy in G[node]:
        if next not in visited:
            queue.append((next, x + dx, y + dy))


for i in range(1, n + 1):
    if ans[i] is None:
        print("undecidable")
        continue
    print(*ans[i])
