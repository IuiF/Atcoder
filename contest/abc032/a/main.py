from math import gcd


a = int(input())
b = int(input())
n = int(input())
lcm = a * b // gcd(a, b)

if lcm >= n:
    print(lcm)
else:
    print((n // lcm) * lcm if n % lcm == 0 else (n // lcm + 1) * lcm)
