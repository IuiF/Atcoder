H, W = map(int, input().split())
S = []
for _ in range(H):
    tmp = list(input())
    if tmp.count("#") == 0:
        H -= 1
        continue
    S.append(tmp)

print(S)

rm_columns = []

for i in range(W):
    if S[0][i] == ".":
        for j in range(1, H):
            if S[j][i] == "#":
                break
            elif S[j][i] == "." and j == H - 1:
                rm_columns.append(i)

print(rm_columns)
