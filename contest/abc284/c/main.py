from collections import deque


n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
q = set()
ans = 0
queue = deque([])
for i in range(1, n + 1):
    if i not in q:
        q.add(i)
        ans += 1
    queue.append(i)
    while queue:
        p = queue.popleft()
        for j in G[p]:
            if j not in q:
                queue.append(j)
                q.add(j)

print(ans)
