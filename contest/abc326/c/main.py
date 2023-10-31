n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

l, r = 0, 0
ans = 0

while r < n:
    while r < n and a[r] - a[l] < m:
        r += 1
    ans = max(ans, r - l)
    l += 1


print(ans)
