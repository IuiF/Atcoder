a, b = map(int, input().split())
c, d = map(int, input().split())
c -= a
d -= b

if c == d == 0:
    print(0)
elif c + d <= 3 or c == d:
    print(1)
else:
    if c == 0 or d == 0:
        print(2)
