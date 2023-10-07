n, m = map(int, input().split())
a = list(map(int, input().split()))
s = []
t = []
for j in range(n):
    tmp = list(input())
    sc = 0
    sp = []
    for i in range(m):
        if tmp[i] == "o":
            sc += a[i]
        else:
            sp.append(a[i])
    sc += j + 1
    s.append(sc)
    t.append(sp)

MAX = max(s)
for i in range(n):
    if s[i] == MAX:
        print(0)
    else:
        t[i].sort(reverse=True)
        ans = 0
        q = MAX - s[i]
        for j in t[i]:
            q -= j
            ans += 1
            if q < 0:
                break
        print(ans)
