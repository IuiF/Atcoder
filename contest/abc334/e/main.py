import sys

sys.setrecursionlimit(10**6)


def modinv(p, q):
    MOD = 998244353
    q_inv = pow(q, -1, MOD)
    return (p * q_inv) % MOD


def dfs(grid, x, y, h, w, num):
    if not (0 <= x < h) or not (0 <= y < w) or grid[x][y] != "#":
        return
    grid[x][y] = num
    dfs(grid, x + 1, y, h, w, num)
    dfs(grid, x - 1, y, h, w, num)
    dfs(grid, x, y + 1, h, w, num)
    dfs(grid, x, y - 1, h, w, num)


def count_diff_nums(grid, x, y, h, w):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    nums = set()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and isinstance(grid[nx][ny], int):
            nums.add(grid[nx][ny])
    return len(nums)


h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
num = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            dfs(grid, i, j, h, w, num)
            num += 1

p = 0
q = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == ".":
            q += 1
            p += num - count_diff_nums(grid, i, j, h, w) + 1

print(modinv(p, q))
