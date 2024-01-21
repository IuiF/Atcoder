n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[1] = abs(a[0] - a[1])

for i in range(2, n):
    dp[i] = min(dp[i - 1] + abs(a[i - 1] - a[i]), dp[i - 2] + abs(a[i - 2] - a[i]))

print(dp[-1])
