h, w, n = map(int, input().split())
cards = []
r = set()
c = set()
for i in range(n):
    y, x = map(int, input().split())
    cards.append([y, x, i])
    r.add(y)
    c.add(x)
r = sorted(list(r))
c = sorted(list(c))
r_dic = {row: idx + 1 for idx, row in enumerate(r)}
c_dic = {col: idx + 1 for idx, col in enumerate(c)}

ans = []
for i in cards:
    y = r_dic[i[0]]
    x = c_dic[i[1]]
    ans.append([y, x, i[2]])
ans.sort(key=lambda x: x[2])

for i, j, _ in ans:
    print(i, j)
