n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
t = 0
M = min(a, b, c, d, e)
if n % M == 0:
    t += n // M
else:
    t += n // M + 1
t += 4
print(t)
