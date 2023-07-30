from collections import defaultdict


x_dic = defaultdict(int)
y_dic = defaultdict(int)

for i in range(3):
    x, y = map(int, input().split())
    x_dic[x] += 1
    y_dic[y] += 1

ans = []
for k, v in x_dic.items():
    if v == 1:
        ans.append(k)
for k, v in y_dic.items():
    if v == 1:
        ans.append(k)

print(*ans)
