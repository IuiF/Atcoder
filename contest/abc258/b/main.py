n = int(input())
a = [list(input()) for _ in range(n)]
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]
max_value = 0
for i in range(n):
    for j in range(n):
        for k in range(8):
            tmp = a[i][j]
            for _ in range(n - 1):
                i += dx[k]
                j += dy[k]
                if i < 0:
                    i += n
                elif i >= n:
                    i -= n
                if j < 0:
                    j += n
                elif j >= n:
                    j -= n
                tmp += a[i][j]
            max_value = max(max_value, int(tmp))

print(max_value)
