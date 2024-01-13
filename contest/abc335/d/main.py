n = int(input())
grid = [[None for _ in range(n)] for _ in range(n)]
pos = [0, 0]
q = 1
r = "E"

while True:
    if q == n**2:
        grid[pos[0]][pos[1]] = "T"  # type: ignore
        break

    grid[pos[0]][pos[1]] = q  # type: ignore
    q += 1

    if r == "E":
        if pos[1] + 1 < n and grid[pos[0]][pos[1] + 1] is None:
            pos[1] += 1
        else:
            r = "S"
            q -= 1
    elif r == "S":
        if pos[0] + 1 < n and grid[pos[0] + 1][pos[1]] is None:
            pos[0] += 1
        else:
            r = "W"
            q -= 1
    elif r == "W":
        if pos[1] - 1 >= 0 and grid[pos[0]][pos[1] - 1] is None:
            pos[1] -= 1
        else:
            r = "N"
            q -= 1
    elif r == "N":
        if pos[0] - 1 >= 0 and grid[pos[0] - 1][pos[1]] is None:
            pos[0] -= 1
        else:
            r = "E"
            q -= 1


for i in grid:
    print(*i)
