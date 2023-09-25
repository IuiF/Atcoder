n = int(input())
a = []
b = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([x, i])
    b.append([y, i])
ans = 10**10
for i in range(len(a)):
    for j in range(len(b)):
        if i == j:
            ans = min(ans, (a[i][0] + b[j][0]))
        else:
            ans = min(ans, max(a[i][0], b[j][0]))
print(ans)
