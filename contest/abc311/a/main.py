N = int(input())
S = list(input())
st = set()

for i in range(N):
    if S[i] not in st:
        st.add(S[i])
    if len(st) == 3:
        print(i + 1)
        exit()
