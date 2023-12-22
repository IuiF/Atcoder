from collections import deque

s = deque(list(input()))
n = int(input())
p = 0
for _ in range(n):
    a = list(input().split())
    if a[0] == "1":
        p += 1
    else:
        if p % 2 == 1:
            if a[1] == "1":
                s.append(a[2])
            else:
                s.appendleft(a[2])
        else:
            if a[1] == "1":
                s.appendleft(a[2])
            else:
                s.append(a[2])
if p % 2 == 0:
    print(*s, sep="")
else:
    s = list(s)[::-1]
    print(*s, sep="")
