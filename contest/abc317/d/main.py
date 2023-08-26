n = int(input())
taka = 0
aoki = 0
ls = []
for _ in range(n):
    a, b, c = map(int, input().split())
    if a < b:
        aoki += c
        tmp = ((a + b) // 2 + 1) - a
        ls.append([tmp, c])
    else:
        taka += c
need = (aoki - taka) // 2 + 1

if need <= 0:
    print(0)
else:
    max_cost = sum(item[1] for item in ls)
    dp = [[float("inf") for _ in range(max_cost + 1)] for _ in range(n + 1)]

    for i in range(len(ls) + 1):
        dp[i][0] = 0

    for i in range(1, len(ls) + 1):
        value, cost = ls[i - 1]
        for j in range(max_cost + 1):
            if j - cost >= 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - cost] + value)
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
    ans = float("inf")
    for i in range(need, max_cost + 1):
        ans = min(ans, dp[len(ls)][i])
    print(ans)
    print(dp)
