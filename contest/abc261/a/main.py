A, B, C, D = map(int, input().split())
arr = [0 for _ in range(101)]
for i in range(A, B):
    arr[i] += 1
for i in range(C, D):
    arr[i] += 1

print(arr.count(2))
