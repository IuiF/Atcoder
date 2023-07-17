H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

ans = []

for i in range(H):
    for j in range(W):
        if A[i][j] % 2 == 1 and j != W - 1:
            ans.append([i + 1, j + 1, i + 1, j + 2])
            A[i][j] -= 1
            A[i][j + 1] += 1
        elif A[i][j] % 2 == 1 and i != H - 1:
            ans.append([i + 1, j + 1, i + 2, j + 1])
            A[i][j] -= 1
            A[i + 1][j] += 1
        else:
            continue

print(len(ans))
for i in ans:
    print(*i)
# print(A)
