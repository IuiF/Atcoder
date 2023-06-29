A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())

for i in range(N):
    tmp = int(input())
    for j in range(3):
        for k in range(3):
            if tmp == A[j][k]:
                A[j][k] = "o"

# 行のチェック
for i in range(3):
    if all(A[i][j] == "o" for j in range(3)):
        print("Yes")
        exit()

# 列のチェック
for j in range(3):
    if all(A[i][j] == "o" for i in range(3)):
        print("Yes")
        exit()

# 対角線のチェック
if all(A[i][i] == "o" for i in range(3)) or all(A[i][2 - i] == "o" for i in range(3)):
    print("Yes")
    exit()

print("No")
