a, b, c, x, y = map(int, input().split())
ans = 0
if a + b >= c * 2:
    ans += min(x, y) * 2 * c
    if x >= y:
        ans += min((x - y) * a, (x - y) * 2 * c)
    else:
        ans += min((y - x) * b, (y - x) * 2 * c)
else:
    ans += a * x + b * y
print(ans)
