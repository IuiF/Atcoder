N = int(input())
x = list(map(int, input().split()))
ans = []
tmp_0 = 0
tmp_1 = 0
tmp_2 = []

for i in x:
    tmp_0 += abs(i)
    tmp_1 += abs(i) ** 2
    tmp_2.append(abs(i))

tmp_1 **= 1 / 2

ans.append(tmp_0)
ans.append(tmp_1)
ans.append(max(tmp_2))

print(*ans, sep="\n")
