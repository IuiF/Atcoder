n, m = map(int, input().split())
sc = []
ans = [-1 for _ in range(n)]

for _ in range(m):
    tmp = tuple(map(int, input().split()))

    if tmp == (1, 0) and n != 1:
        print(-1)
        exit()

    sc.append(tmp)
sc = list(set(sc))

for i in range(len(sc)):
    if ans[sc[i][0] - 1] != -1:
        print(-1)
        exit()
    else:
        ans[sc[i][0] - 1] = sc[i][1]

for i in range(len(ans)):
    if ans[i] == -1:
        ans[i] = 0

if ans[0] == 0 and len(ans) != 1:
    ans[0] = 1


print(*ans, sep="")
