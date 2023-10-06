import math


n = int(input())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
ans = 0
p = 0
for i in a:
    if p % 2 == 0:
        ans += i**2
        p += 1
    else:
        ans -= i**2
        p += 1
ans = ans * math.pi
print(ans)
