n = int(input())
ans = 0
st = set()
for _ in range(n):
    tmp = input()
    if tmp in st:
        ans += 1
    else:
        st.add(tmp)
print(ans)
