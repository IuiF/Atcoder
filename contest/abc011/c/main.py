n = int(input())
ng = list(int(input()) for _ in range(3))
count = 0

if n in ng:
    print("NO")
    exit()

while True:
    if n - 3 not in ng:
        n -= 3
        count += 1
    elif n - 2 not in ng:
        n -= 2
        count += 1
    elif n - 1 not in ng:
        n -= 1
        count += 1
    else:
        print("NO")
        exit()
    if n <= 0:
        break

if count <= 100:
    print("YES")
else:
    print("NO")
