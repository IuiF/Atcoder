w, h, n = map(int, input().split())
x0, x1, y0, y1 = 0, w, 0, h
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        x0 = max(x, x0)
    elif a == 2:
        x1 = min(x, x1)
    elif a == 3:
        y0 = max(y, y0)
    else:
        y1 = min(y, y1)
if x0 >= x1 or y0 >= y1:
    print(0)
else:
    print(abs((x1 - x0) * (y1 - y0)))
