h, m = map(int, input().split())
a, b = h // 10, h % 10
c, d = m // 10, m % 10

while True:
    if 0 <= a * 10 + c <= 23 and 0 <= b * 10 + d <= 59:
        break
    else:
        m += 1
        if m == 60:
            h, m = h + 1, 0
        if h == 24:
            h = 0
        a, b = h // 10, h % 10
        c, d = m // 10, m % 10
print(a * 10 + b, c * 10 + d)
