n, m = map(int, input().split())
x = list(map(int, input().split()))
y = []
for i in range(1, m):
    a = abs(x[i] - x[i - 1])
    b = n - a
    y.append((a, b))

print(y)
