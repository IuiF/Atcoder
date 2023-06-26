n, a, b = map(int, input().split())
if n % (a + b) > a:
    print((n // (a + b)) * a + a)
else:
    print((n // (a + b)) * a + n % (a + b))
