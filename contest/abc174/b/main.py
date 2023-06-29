n, d = map(int, input().split())
count = 0
for _ in range(n):
    a, b = map(int, input().split())
    if d**2 >= a**2 + b**2:
        count += 1
print(count)
