x1, y1, x2, y2 = map(int, input().split())

x2x1 = x2 - x1
y2y1 = y2 - y1

x3 = x2 - y2y1
y3 = y2 + x2x1

x4 = x3 - x2x1
y4 = y3 - y2y1

print(x3, y3, x4, y4)
