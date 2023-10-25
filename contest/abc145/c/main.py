import itertools


def length(a, b, c, d):
    ans = ((a - c) ** 2 + (b - d) ** 2) ** 0.5
    return ans


n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
ar = [i for i in range(n)]
arr = list(itertools.permutations(ar))
ans = 0

for i in arr:
    tmp = 0
    for j in range(len(i) - 1):
        tmp += length(x[i[j]][0], x[i[j]][1], x[i[j + 1]][0], x[i[j + 1]][1])
    ans += tmp
ans /= len(arr)

print(ans)
