N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    x, *k = map(int, input().split())
    if x == 1:
        A[k[0] - 1] = k[1]
    else:
        print(A[k[0] - 1])
