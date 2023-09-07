N = int(input())
A = list(map(int, input().split()))[::-1]
tmp = 0
ans = 0
for i in range(N):
    tmp += A[i]
    if tmp == 3:
        ans = len(A[i + 1 :])
        break
    elif tmp > 3:
        ans = len(A[i:])
        break

print(ans)
