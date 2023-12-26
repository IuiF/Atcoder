n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(1, n):
    b.append(a[i] + b[i - 1])

p = 0
q = k
ans = b[k - 1]
while q < n:
    ans += b[q] - b[p]
    p, q = p + 1, q + 1

print(ans)
