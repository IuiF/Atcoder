from math import gcd


N, X = map(int, input().split())
A = list(map(int, input().split()))
A.append(X)
A.sort()

if N == 1:
    print(abs(A[1] - A[0]))
else:
    B = []
    for i in range(N):
        B.append(A[i + 1] - A[i])

    ans = gcd(B[0], B[1])
    for i in range(2, len(B)):
        ans = gcd(ans, B[i])

    print(ans)
