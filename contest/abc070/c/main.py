from math import lcm


n = int(input())
T = int(input())
for _ in range(n - 1):
    Q = int(input())
    T = lcm(T, Q)

print(T)
