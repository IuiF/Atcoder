n, m, x = map(int, input().split())
a = set(map(int, input().split()))
b = 0
c = 0
for i in range(n + 1):
    if i in a and i < x:
        b += 1
    elif i in a and i > x:
        c += 1
print(min(b, c))
