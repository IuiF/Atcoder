H, W = map(int, input().split())
S = []
for _ in range(H):
    tmp = list(input())
    if tmp.count("#") == 0:
        H -= 1
        continue
    S.append(tmp)

rm_columns = []

for i in range(W):
    if S[0][i] == ".":
        for j in range(H):
            if S[j][i] == "#":
                break
            elif S[j][i] == "." and j == H - 1:
                rm_columns.append(i)

rm_columns.sort(reverse=True)

for row in S:
    for column in rm_columns:
        del row[column]


for row in S:
    print(*row, sep="")
