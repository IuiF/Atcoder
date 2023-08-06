n, m = map(int, input().split())
st = set([i + 1 for i in range(n)])
for _ in range(m):
    a, b = map(int, input().split())
    if b in st:
        st.remove(b)

if len(st) == 1:
    print(st.pop())
else:
    print(-1)
