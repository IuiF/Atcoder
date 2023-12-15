n, s, k = map(int, input().split())
ans = 0
for _ in range(n):
    p, q = map(int, input().split())
    ans += p * q
if ans >= s:
    print(ans)
else:
    print(ans + k)
