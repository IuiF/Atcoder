n = int(input())
ans = 0

if n >= 1000:
    ans += n - 999
if n >= 1000**2:
    ans += n - 1000**2 + 1
if n >= 1000**3:
    ans += n - 1000**3 + 1
if n >= 1000**4:
    ans += n - 1000**4 + 1
if n >= 1000**5:
    ans += n - 1000**5 + 1

print(ans)
