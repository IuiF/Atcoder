from decimal import ROUND_HALF_UP, Decimal


A, B = map(int, input().split())
ans = Decimal(str(B / A)).quantize(Decimal("0.000"), rounding=ROUND_HALF_UP)
print(ans)
