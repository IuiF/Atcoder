n, k = map(int, input().split())
A = [0] + list(map(int, input().split()))

pos = 1
tmp = -1
arr = []
st = set()

if k > n:
    while True:
        if A[pos] in st:
            tmp = A[pos]
            break
        st.add(A[pos])
        arr.append(A[pos])
        pos = A[pos]

    n = k - arr.index(A[pos])

    arr = arr[arr.index(tmp) :]

    print(arr[n % len(arr) - 1])
else:
    for _ in range(k):
        pos = A[pos]
    print(pos)
