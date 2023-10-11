n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 1
st = set([x])
for _ in range(n):
    x = a[x - 1]
    if x in st:
        break
    else:
        st.add(x)
        ans += 1
print(ans)
