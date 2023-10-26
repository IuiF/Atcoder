def dfs(i, j, s, visited):
    


h, w = map(int, input().split())
s = [list(input().split()) for _ in range(h)]
visited = set()
ans = 0

for i in range(h):
    for j in range(w):
        if (i, j) in visited:
            continue
        elif s[i][j] == '#':
            ans += 1
            dfs(i, j, s, visited)
