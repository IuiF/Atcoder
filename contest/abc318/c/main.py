n, d, p = map(int, input().split())
f = list(map(int, input().split()))
f.sort(reverse=True)

ans = 0
pos = 0
for i in range(n // d):
    tmp = sum(f[i * d : (i + 1) * d])
    if tmp >= p:
        ans += p
    else:
        ans += tmp

if n % d != 0:
    tmp = sum(f[(n // d) * d :])
    if tmp >= p:
        ans += p
    else:
        ans += tmp

print(ans)
