a, b, k = map(int, input().split())

if a - k < 0 and b - k + a < 0:
    b = 0
    a = 0
elif a - k < 0:
    b = b - k + a
    a = 0
else:
    a = a - k

print(a, b)
