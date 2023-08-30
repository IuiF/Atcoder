import itertools


N, M = map(int, input().split())
cb = list(itertools.combinations([i for i in range(N)], 2))
S = []
for _ in range(N):
    S.append(list(input()))

ans = 0
for i, j in cb:
    if all((S[j][k] == "o" or S[i][k] == "o") for k in range(M)):
        ans += 1

print(ans)
