n = int(input())
c = list(map(int, input().split()))
c.sort()
ans = 1
MOD = 10**9 + 7
for i in range(n):
    ans *= c[i] - i
    ans %= MOD

print(max(0, ans))
