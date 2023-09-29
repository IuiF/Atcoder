a, b = map(int, input().split())
c = 0
for i in range(b - a):
    c += i
print(c - a)
