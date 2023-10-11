n = int(input())
st = set()
for _ in range(n):
    st.add(input())
print("Yes" if len(st) != n else "No")
