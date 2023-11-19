n = int(input())
s = list(input())
ans = 0
tmp = 1
for i in range(n - 1):
    if s[i] == ">":
        tmp += 1
    else:
        ans += (tmp * (tmp - 1)) // 2
        tmp = 1
if s[-1] == ">":
    ans += (tmp * (tmp - 1)) // 2

print(ans)
