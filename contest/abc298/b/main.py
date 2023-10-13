n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

f = False
for _ in range(4):
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and b[i][j] == 0:
                break
