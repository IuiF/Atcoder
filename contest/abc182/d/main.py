n = int(input())
a = list(map(int, input().split()))
b = [0] * n
b[0] = a[0]
for i in range(1, n):
    b[i] = a[i] + b[i - 1]


p = b[0]
bm = max(0, p)
ans = max(0, p)

for i in range(1, n):
    bm = max(bm, b[i])
    bp = p
    p += b[i]
    ans = max(ans, bp + bm, p)

print(ans)
