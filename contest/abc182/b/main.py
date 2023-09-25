n = int(input())
A = list(map(int, input().split()))
B = [0 for _ in range(max(A) + 1)]

for i in range(2, max(A) + 1):
    for j in A:
        if j % i == 0:
            B[i] += 1


print((B.index(max(B))))
