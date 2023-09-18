pos = int(input()) - 1
a = list(map(int, ("0 " + input()).split()))
ans = 0
while pos != 0:
    ans += 1
    pos = a[pos] - 1

print(ans)
