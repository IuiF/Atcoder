def calc_x(x):
    x = r * x - D
    return x


r, D, x = map(int, input().split())

for _ in range(10):
    x = calc_x(x)
    print(x)
