n, m = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
ans = set()
for i in range(n):
    for j in G[i]:
        for k in G[j]:
            if i in G[k]:
                a = tuple(sorted([i, j, k]))
                ans.add(a)
print(len(ans))
