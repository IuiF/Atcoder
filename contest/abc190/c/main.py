n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
b = [list(map(int, input().split())) for _ in range(k)]
ans = 0

for i in range(2**k):
    c = [0] * k
    for j in range(k):
        if (i >> j) & 1:
            c[j] = 1
    st = set()
    for j in range(k):
        st.add(b[j][c[j]])
    t = 0
    for x, y in a:
        if x in st and y in st:
            t += 1
    ans = max(ans, t)

print(ans)
