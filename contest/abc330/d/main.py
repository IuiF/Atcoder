n = int(input())
s = [list(input()) for _ in range(n)]
r_s = list(zip(*s))

col_o = [s[i].count("o") for i in range(n)]
row_o = [r_s[i].count("o") for i in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        if s[i][j] == "o":
            count += (col_o[i] - 1) * (row_o[j] - 1)

print(count)
