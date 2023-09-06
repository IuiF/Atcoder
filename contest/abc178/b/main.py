a, b, c, d = map(int, input().split())
ans = max(a * c, b * d, b * c, a * d)
print(ans)
