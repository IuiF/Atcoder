N = int(input())
A = [0]

for _ in range(N):
    A.append(int(input()))

st = set()
pos = 1
ans = 1
while True:
    if A[pos] == 2:
        print(ans)
        exit()

    if A[pos] in st:
        print(-1)
        exit()

    st.add(A[pos])
    pos = A[pos]
    ans += 1
