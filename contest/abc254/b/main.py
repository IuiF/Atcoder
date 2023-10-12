n = int(input())
ans = [[1]]
for i in range(1, n):
    row = [1]
    for j in range(1, i):
        row.append(ans[i - 1][j - 1] + ans[i - 1][j])
    row.append(1)
    ans.append(row)

for row in ans:
    print(" ".join(str(x) for x in row))
