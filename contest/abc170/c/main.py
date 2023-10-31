x, n = map(int, input().split())
p = list(map(int, input().split()))
ans = []
for i in range(200):
    if i not in p:
        t = abs(i - x)
        ans.append((t, i))
if len(ans) != 0:
    ans.sort(key=lambda x: (x[0], x[1]))
    print(ans[0][1])
else:
    print(x)
