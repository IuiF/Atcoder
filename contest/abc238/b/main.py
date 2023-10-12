n = int(input())
a = list(map(int, input().split()))
f = [True] * 360
f[0] = False
c = 0
for i in range(n):
    c += a[i]
    c = c % 360
    f[c] = False
ans = 0
t = 0
for i in f:
    if i == True:
        t += 1
    else:
        ans = max(ans, t)
        t = 0
ans = max(ans, t)
print(ans + 1)
