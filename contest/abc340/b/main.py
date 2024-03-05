q = int(input())
a = []
for i in range(q):
    q, t = map(int, input().split())
    if q == 1:
        a.append(t)
    else:
        print(a[-t])
