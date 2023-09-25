a, b, c, d = map(int, input().split())
ans = a + ((c - a) / (b + d) * b)
print(ans)
