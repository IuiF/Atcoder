x, k = map(int, input().split())
for i in range(k):
    d = 10 ** (i + 1)
    q, r = divmod(x, d)
    if r >= 5 * (10**i):
        q += 1
    x = q * d

print(x)
