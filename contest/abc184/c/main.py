a, b = map(int, input().split())
c, d = map(int, input().split())
c -= a
d -= b
c = abs(c)
d = abs(d)


if c == d == 0:
    print(0)
elif c + d <= 3 or c == d:
    print(1)
else:
    if (c - d) % 2 == 0 or (max(c, d) - min(c, d)) <= 3 or c + d <= 6:
        print(2)
    else:
        print(3)
