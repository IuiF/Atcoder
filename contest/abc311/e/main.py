H, W, N = map(int, input().split())
M = [[1 for _ in range(W)] for _ in range(H)]
for _ in range(N):
    a, b = map(int, input().split())
    M[a - 1][b - 1] = 0


print()
