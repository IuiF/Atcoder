a, b = map(int, input().split())

for i in range(1, 10001):
    if int(i * 8 / 100) == a and int(i / 10) == b:
        print(i)
        exit()
print(-1)
