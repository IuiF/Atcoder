n = int(input())
d, x = map(int, input().split())
for _ in range(n):
    t = int(input())
    for i in range(100):
        if i * t + 1 <= d:
            x += 1
        else:
            break
print(x)
