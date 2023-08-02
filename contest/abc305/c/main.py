h, w = map(int, input().split())
grid, cookie = [], []
x, y = 0, 0

for i in range(h):
    grid.append(input())
    cookie.append(grid[i].count('#'))

y = cookie.index(max(cookie)-1)

for i, c in enumerate(grid[y]):
    if c == '.' and ((y > 0 and grid[y-1][i] == '#') or (y < h-1 and grid[y+1][i] == '#')): # 上下の端でエラーが起きてた
        x = i

print(y+1, x+1)
