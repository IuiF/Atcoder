n, q = map(int, input().split())
a = list(map(int, input().split()))
dic_s = {i: 0 for i in range(n + 2)}
dic_p = {i + 1: a[i] for i in range(len(a))}
for i in a:
    dic_s[i] += 1
st = sorted(list(set(a)))
M = set()
for i in range(n + 1):
    if i not in st:
        M.add(i)
ans = min(M)

for _ in range(q):
    x, y = map(int, input().split())
    if y > n + 1:
        y = n + 1
    t = dic_p[x]
    dic_p[x] = y
    dic_s[t] -= 1
    dic_s[y] += 1
    if dic_s[t] == 0:
        M.add(t)
    M.discard(y)
