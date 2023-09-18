n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for i in range(1, n + 1):
    ans = []
    ans.append(len(G[i]))
    ans.append(sorted(G[i]))
    if ans[0] == 0:
        print(0)
    else:
        print(ans[0], end=" ")
        print(*ans[1])
