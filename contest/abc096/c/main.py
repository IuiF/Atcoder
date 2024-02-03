h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]


for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            up = s[i - 1][j] if i > 0 else None
            down = s[i + 1][j] if i < h - 1 else None
            left = s[i][j - 1] if j > 0 else None
            right = s[i][j + 1] if j < w - 1 else None

            if not any([up == "#", down == "#", left == "#", right == "#"]):
                print("No")
                exit()
print("Yes")
