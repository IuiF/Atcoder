N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

fg = False

for i in G[1]:
    if N in G[i]:
        fg = True


print("POSSIBLE" if fg else "IMPOSSIBLE")
