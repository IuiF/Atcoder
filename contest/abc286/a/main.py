N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
for i in range(Q - P + 1):
    A[P - 1 + i], A[R - 1 + i] = A[R - 1 + i], A[P - 1 + i]
print(*A)
