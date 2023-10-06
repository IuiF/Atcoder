n, a, b = map(int, input().split())
pos = 0
for _ in range(n):
    j, k = input().split()
    k = int(k)
    if k < a:
        if j[0] == "W":
            pos -= a
        else:
            pos += a
    elif k > b:
        if j[0] == "W":
            pos -= b
        else:
            pos += b
    else:
        if j[0] == "W":
            pos -= k
        else:
            pos += k
if pos == 0:
    print(0)
elif pos < 0:
    print("West", -pos)
else:
    print("East", pos)
