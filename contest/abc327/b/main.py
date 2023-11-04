n = int(input())
for i in range(1, 30):
    if i**i == n:
        print(i)
        exit()
print(-1)
