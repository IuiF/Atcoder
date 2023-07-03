N, M = map(int, input().split())
A, B = [], []

for _ in range(N):
    A.append(list(input()))

for _ in range(M):
    B.append(list(input()))

f = False
for i in range(N - M + 1):
    for j in range(N - M + 1):
        if all(A[i + x][j + y] == B[x][y] for x in range(M) for y in range(M)):
            print("Yes")
            exit()
print("No")
