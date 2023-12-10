k, g, m = map(int, input().split())
t = [0, 0]

for _ in range(k):
    if t[0] == g:
        t[0] = 0
    elif t[1] == 0:
        t[1] = m
    else:
        a = min(g - t[0], t[1])
        t[0] += a
        t[1] -= a

print(t[0], t[1])
