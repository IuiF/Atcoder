n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]


for _ in range(4):
    a = [list(reversed(col)) for col in zip(*a)]
    t = True
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and b[i][j] == 0:
                t = False
                break
        if not t:
            break
    if t:
        print("Yes")
        exit()
print("No")
