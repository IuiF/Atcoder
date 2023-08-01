from decimal import Decimal, ROUND_HALF_UP

X = Decimal(input())
print(X.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
