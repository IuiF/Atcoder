a, b, c, k = map(int, input().split())
if k > a + b:
    print(a - (k - a - b))
elif k < a:
    print(k)
else:
    print(a)
