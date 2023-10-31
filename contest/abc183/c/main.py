import itertools

n, k = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(n)]
ar = [i for i in range(1, n)]
route = list(itertools.permutations(ar))
ans = 0

for i in route:
    tmp = 0
    tmp += T[0][i[0]]
    for j in range(1, len(i)):
        tmp += T[i[j - 1]][i[j]]
    tmp += T[i[-1]][0]
    if tmp == k:
        ans += 1

print(ans)
