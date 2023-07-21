from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


N = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
M = 1

for i in a:
    M = lcm(M, i)

M -= 1

for i in a:
    ans += M % i

print(ans)
