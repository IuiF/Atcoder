n, m, d = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
b = list(map(int, input().split()))
b.sort(reverse=True)
pa, pb = 0, 0
ans = -1
while pa < n and pb < m:
    if abs(a[pa] - b[pb]) <= d:
        ans = a[pa] + b[pb]
        break
    elif a[pa] < b[pb]:
        pb += 1
    elif a[pa] > b[pb]:
        pa += 1

print(ans)
