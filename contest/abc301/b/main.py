Num = int(input())
A = list(map(int, input().split()))
answer = []

for i in range(1, Num):
    if A[i - 1] < A[i]:
        j = A[i - 1]
        while j != A[i]:
            answer.append(j)
            j += 1
    if A[i - 1] > A[i]:
        j = A[i - 1]
        while j != A[i]:
            answer.append(j)
            j -= 1
answer.append(A[-1])

print(*answer)
