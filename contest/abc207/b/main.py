a, b, c, d = map(int, input().split())
if b / c < d:
    e = 0
    for i in range(10**6):
        a += b
        e += c
        if a / e <= d:
            print(i + 1)
            break

else:
    print(-1)
