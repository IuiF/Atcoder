n, x = map(int, input().split())
y = bin(x)[2:][::-1]
a = list(map(int, input().split()))
ans = 0
for i in range(len(y)):
    if y[i] == "1":
        ans += a[i]
print(ans)
