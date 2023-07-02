N, M = map(int, input().split())
H = list(map(int, input().split()))
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

ans = 0
for i in range(1, N + 1):
    fg = True
    for j in G[i]:
        if H[i - 1] <= H[j - 1]:
            fg = False
    if fg:
        ans += 1


print(ans)
