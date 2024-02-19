from decimal import Decimal

r, x, y = map(Decimal, input().split())
L = (x**2 + y**2) ** Decimal("0.5")
if L < r:
    print(2)
elif L % r == 0:
    print(L // r)
else:
    print(L // r + 1)
