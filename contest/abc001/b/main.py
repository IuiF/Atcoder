x = float(input()) / 1000
ans = "00"

if 0.1 <= x <= 5:
    x *= 10
elif 6 <= x <= 30:
    x += 50
elif 35 <= x <= 70:
    x -= 30
    x /= 5
    x += 80
elif 70 < x:
    x = 89

ans = "{:02d}".format(int(x))

print(ans)
