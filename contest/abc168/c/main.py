import math

A, B, H, M = map(int, input().split())
rad = math.radians(abs((H * 30 + 30 * M / 60) - (M * 6)))
Ans = math.sqrt(A**2 + B**2 - (2 * A * B * math.cos(rad)))

print(Ans)
