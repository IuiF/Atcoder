N, L = map(int, input().split())
ans = 0
b = 10**10
for i in range(1, N + 1):
    a = L + i - 1
    b = a if abs(a) < abs(b) else b
    ans += a
ans -= b

print(ans)
