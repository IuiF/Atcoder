a = [list(map(int, input().split())) for _ in range(9)]

flag = True

for row in a:
    if len(set(row)) != 9 or min(row) != 1 or max(row) != 9:
        flag = False
        break

for j in range(9):
    col = [a[i][j] for i in range(9)]
    if len(set(col)) != 9 or min(col) != 1 or max(col) != 9:
        flag = False
        break

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        tmp = [a[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
        if len(set(tmp)) != 9 or min(tmp) != 1 or max(tmp) != 9:
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")
