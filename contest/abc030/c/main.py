n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pos = [0, 0, 0]
time = 0
ans = 0
while pos[0] < n and pos[1] < m:
    if pos[2] == 0:
        if a[pos[0]] >= time:
            time = a[pos[0]] + x
            pos[2] = 1
        else:
            pos[0] += 1
    else:
        if b[pos[1]] >= time:
            time = b[pos[1]] + y
            pos[2] = 0
            ans += 1
            pos[0] += 1
        pos[1] += 1

print(ans)
