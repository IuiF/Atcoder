N = int(input())
A = list(map(int, input().split()))
G = [0 for _ in range(N)]
for i in range(N - 1):
    G[A[i] - 1] += 1

print(*G, sep="\n")
