N, M = map(int, input().split())
A, B = [], []

for _ in range(N):
    A.append(list(input()))

for _ in range(M):
    B.append(list(input()))

print(A, B)
