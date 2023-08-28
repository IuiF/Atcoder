n = int(input())
t = list(input())
p = [0, 0]
vi = 0
v = [[1, 0], [0, -1], [-1, 0], [0, 1]]

for i in t:
    if i == "S":
        p[0] += v[vi % 4][0]
        p[1] += v[vi % 4][1]
    else:
        vi += 1
print(*p)
