def counter(a):
    ans = 0
    for i in range(1, a + 1):
        ans += i
    return ans


n = int(input())
a = list(map(int, input().split()))
ans = 0


t = a[0]
c = 1
for i in range(1, n):
    if a[i] > t:
        c += 1
    else:
        ans += counter(c)
        c = 1
    t = a[i]
ans += counter(c)

print(ans)
