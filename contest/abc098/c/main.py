N = int(input())
ls = list(input())
WE_ls = [[0, 0] for _ in range(N + 1)]

for i in range(1, len(ls) + 1):
    if ls[i - 1] == "E":
        WE_ls[i] = [WE_ls[i - 1][0], WE_ls[i - 1][1] + 1]
    else:
        WE_ls[i] = [WE_ls[i - 1][0] + 1, WE_ls[i - 1][1]]

ans = 10**10

for i in range(N + 1):
    ans = min(ans, WE_ls[i][0] + (WE_ls[-1][1] - WE_ls[i][1]))


print(ans)
