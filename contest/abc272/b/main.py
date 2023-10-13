n, m = map(int, input().split())
f = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
    k, *a = map(int, input().split())
    for i in a:
        for j in a:
            f[i - 1][j - 1] = True
            f[j - 1][i - 1] = True
if all(len(f[i]) == sum(f[i]) for i in range(n)):
    print("Yes")
else:
    print("No")
