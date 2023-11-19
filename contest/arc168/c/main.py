from collections import defaultdict

MOD = 998244353
n, k = map(int, input().split())
s = input()
dic = defaultdict(int)

for char in s:
    dic[char] += 1

dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(k + 1):
        dp[i][j] = dp[i - 1][j]

        if j > 0:
            for char in "ABC":
                if char != s[i - 1]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * dic[char]) % MOD

    dic[s[i - 1]] -= 1

print(sum(dp[n]) % MOD)
