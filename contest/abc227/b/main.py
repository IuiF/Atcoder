n = int(input())
s = list(map(int, input().split()))
st = set(s)
for i in range(1, 251):
    for j in range(1, 501):
        tmp = 4 * i * j + 3 * i + 3 * j
        if tmp in st:
            st.remove(tmp)
print(sum(s.count(i) for i in st))
