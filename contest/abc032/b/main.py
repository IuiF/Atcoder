s = input()
k = int(input())
st = set()
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        st.add(s[i:j])

print(sum(1 for i in st if len(i) == k))
