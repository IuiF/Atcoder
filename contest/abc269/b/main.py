s = [list(input()) for _ in range(10)]
a, b, c, d = -1, -1, -1, -1
for i in range(10):
    if s[i].count("#") and a == -1:
        a = i + 1
        for j in range(10):
            if s[i][j] == "#" and c == -1:
                c = j + 1
            if s[i][j] == "." and c != -1 and d == -1:
                d = j
    if not s[i].count("#") and a != -1 and b == -1:
        b = i
if b == -1:
    b = 10
if d == -1:
    d = 10

print(a, b)
print(c, d)
