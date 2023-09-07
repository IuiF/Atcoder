n, k, q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in range(q):
    if A[L[i] - 1] == n:
        continue
    elif L[i] == k:
        A[L[i] - 1] += 1
    elif A[L[i] - 1] + 1 != A[L[i]]:
        A[L[i] - 1] += 1
    else:
        continue

print(*A)
