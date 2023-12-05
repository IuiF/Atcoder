n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: (x[0]))
i = 0

while i < n:
    if a[i][0] <= k:
        k += a[i][1]
        i += 1
    else:
        break

print(k)
