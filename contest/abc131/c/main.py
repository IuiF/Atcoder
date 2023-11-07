from math import lcm


a, b, c, d = map(int, input().split())
a -= 1
aa = a + a // lcm(c, d) - a // c - a // d
bb = b + b // lcm(c, d) - b // c - b // d

print(bb - aa)
