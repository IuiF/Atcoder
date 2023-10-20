n = int(input())
a = list(map(int, input().split()))
d = dict()
tmp = 0
for i in range(n):
    d[i + 1] = a[i]
ans = 0
for i in d.keys():
    if i == d[i]:
        tmp += 1
    elif i == d[d[i]]:
        ans += 1
print(ans // 2 + (tmp * (tmp - 1)) // 2)
