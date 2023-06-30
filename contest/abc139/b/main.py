a, b = map(int, input().rstrip().split())
ans = 1


if b == 1:
    print(0)
    exit()
elif b - a <= 0:
    print(ans)
    exit()

b -= a

while b > 0:
    ans += 1
    b -= a - 1


print(ans)
