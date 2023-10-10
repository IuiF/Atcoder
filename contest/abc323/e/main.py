MOD = 998244353
n, x = map(int, input().split())
r = list(map(int, input().split()))
f = r[0]
r.sort()
m = [0 for _ in range(x + 1)]
m[0] = pow(n, -1, MOD)

for i in range(1, x + 1):
    for j in r:
        if i - j < 0:
            continue
        elif i - j == 0:
            m[i] += pow(n, -1, MOD)
        else:
            m[i] += m[i - j] * pow(n, -1, MOD)
        m[i] %= MOD
ans = 0
for i in range(f):
    if x - i < 0:
        continue
    elif x - i == 0:
        ans += pow(n, -1, MOD)
    else:
        ans += m[x - i] * pow(n, -1, MOD)
    ans %= MOD

print(ans)
