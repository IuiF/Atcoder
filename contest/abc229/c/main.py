n, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: -x[0])
ans = 0
for i, j in a:
    if w >= j:
        w -= j
        ans += i * j
    else:
        ans += i * w
        break


print(ans)
