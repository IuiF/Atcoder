import math

a, b = map(int, input().split())
Ans = a * b // math.gcd(a, b)  # math.lcmは3.9以降にしかないためREを吐く

print(Ans)
