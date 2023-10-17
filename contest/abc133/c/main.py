l, r = map(int, input().split())
if r - l >= 2019:
    print(0)
else:
    ans = 2020
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            t = i * j
            ans = min(ans, t % 2019)
    print(ans)
