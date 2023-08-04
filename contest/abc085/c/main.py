N, total = map(int, input().split())
Ans = [-1, -1, -1]

for i in range(N + 1):
    for j in range(N + 1 - i):
        if 10000 * i + 5000 * j + 1000 * (N - i - j) == total:
            Ans = [i, j, N - i - j]

print(*Ans)
