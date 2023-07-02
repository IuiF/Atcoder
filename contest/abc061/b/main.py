N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(1, N + 1):
    print(len(G[i]))
