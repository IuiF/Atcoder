N = int(input())

W = input()
st = set()
st.add(W)

for _ in range(N - 1):
    tmp = input()
    if tmp not in st and W[-1] == tmp[0]:
        st.add(tmp)
        W = tmp
        continue
    else:
        print("No")
        exit()
print("Yes")
