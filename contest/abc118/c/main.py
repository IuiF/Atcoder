n = int(input())
a = list(map(int, input().split()))
b = []

while len(a) > 1:
    a.sort()
    t = a[0]
    b = []
    for i in range(1, len(a)):
        if a[i] % t != 0:
            b.append(a[i] % t)
    b.append(t)
    a = b

print(*b)
