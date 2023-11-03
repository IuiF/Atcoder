def pow_mod(x, y, m):
    a = 1
    while y > 0:
        a *= x
        a %= m
        y -= 1
    return a


n = int(input())
MOD = 10**9 + 7
if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    ans = (
        pow_mod(10, n, MOD)
        - pow_mod(9, n, MOD)
        - pow_mod(9, n, MOD)
        + pow_mod(8, n, MOD)
    )
    ans += MOD
    ans %= MOD
    print(ans)
