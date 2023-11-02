s = list(input())
c = "chokudai"
dp = [[0 for _ in range(8)] for _ in range(len(s))]
if s[0] == c[0]:
    dp[0][0] = 1

for i in range(1, len(s)):
    for j in range(8):
        if s[i] == c[j]:
            if j == 0:
                dp[i][j] = dp[i - 1][j] + 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        else:
            if j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

# print(dp)
print(dp[-1][-1] % (10**9 + 7))
