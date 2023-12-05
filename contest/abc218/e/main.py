n, m = map(int, input().split())
S = []
f = {i: False for i in range(1, n + 1)}
st = set()
ans = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    S.append((min(a, b), max(a, b), c))
    ans += c

S.sort(key=lambda x: (-x[2]))
bns = 0

for _ in range(m):
    a, b, c = S.pop()
    if c < 0:
        st.add((a, b))
        f[a], f[b] = True, True
        bns += c
    elif (a, b) in st or (f[a] == True and f[b] == True):
        continue
    elif len(st) == n - 1:
        break
    else:
        st.add((a, b))
        f[a], f[b] = True, True
        bns += c


print(ans - bns)
