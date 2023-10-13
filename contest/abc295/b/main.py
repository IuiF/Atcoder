r, c = map(int, input().split())
m = [list(input()) for _ in range(r)]
nums = []
for i in range(r):
    for j in range(c):
        if m[i][j].isdigit():
            nums.append((int(i), int(j), int(m[i][j])))

dx = [-1, -1, 1, 1]
dy = [1, -1, 1, -1]
for i in nums:
    for j in range(4):
        for k in range(i[2] + 1):
            for l in range(i[2] + 1):
                if abs(k * dx[j]) + abs(l * dy[j]) <= i[2]:
                    x = i[0] + k * dx[j]
                    y = i[1] + l * dy[j]
                    if x < 0 or x >= r:
                        continue
                    elif y < 0 or y >= c:
                        continue
                    else:
                        m[x][y] = "."

for i in m:
    print("".join(i))
