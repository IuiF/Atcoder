S = list(input())
ans = 0
a = [0, 0, 0, 0, 0]
for i in S:
    if i == "L":
        a[0] += 1
    elif i == "R":
        a[1] += 1
    elif i == "U":
        a[2] += 1
    elif i == "D":
        a[3] += 1
    else:
        a[4] += 1
t = max(a[0], a[1]) - min(a[0], a[1]) + max(a[2], a[3]) - min(a[2], a[3])
if int(input()) == 1:
    ans = t + a[4]
else:
    if t >= a[4]:
        ans = t - a[4]
    else:
        if (a[4] - t) % 2 == 0:
            ans = 0
        else:
            ans = 1
print(ans)
