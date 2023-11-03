n = int(input())
a = list(map(int, input().split()))
MOD = 10**9 + 7

cumulative_sum = [0] * (n + 1)
for i in range(n):
    cumulative_sum[i + 1] = cumulative_sum[i] + a[i]

ans = 0
for i in range(n):
    ans += a[i] * (cumulative_sum[n] - cumulative_sum[i + 1])
    ans %= MOD

print(ans)
