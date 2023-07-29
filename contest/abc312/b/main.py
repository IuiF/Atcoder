def match(grid, i, j):
    for dx in range(3):
        for dy in range(3):
            if grid[i + dx][j + dy] != "#" or grid[i + dx + 6][j + dy + 6] != "#":
                return False

    for dx, dy in [
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
        (5, 5),
        (5, 6),
        (5, 7),
        (5, 8),
        (6, 5),
        (7, 5),
        (8, 5),
    ]:
        if grid[i + dx][j + dy] != ".":
            return False

    return True


N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
ans = []

for i in range(N - 8):
    for j in range(M - 8):
        if match(grid, i, j):
            ans.append((i + 1, j + 1))

for i in ans:
    print(*i)
