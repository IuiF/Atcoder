N, M = map(int, input().split())
A = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    P = tmp[0]
    C = tmp[1]
    F_set = set(tmp[2:])
    A.append([P, C, F_set])


for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if (
            A[i][0] == A[j][0]
            and (A[i][2].issubset(A[j][2]) or A[j][2].issubset(A[i][2]))
            and A[i][2] != A[j][2]
        ):
            print("Yes")
            exit()
        if (A[i][0] > A[j][0] and A[i][2].issubset(A[j][2])) or (
            A[i][0] < A[j][0] and A[j][2].issubset(A[i][2])
        ):
            print("Yes")
            exit()
print("No")
