n, m = map(int, input().split())
n %= 12
a = n * 30 + m * 0.5
b = m * 6
print(min(max(a, b) - min(a, b), 360 - max(a, b) + min(a, b)))
