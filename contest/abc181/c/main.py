def is_collinear(x1, y1, x2, y2, x3, y3):
    return (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2)


n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if is_collinear(x[i][0], x[i][1], x[j][0], x[j][1], x[k][0], x[k][1]):
                print("Yes")
                exit()
print("No")
