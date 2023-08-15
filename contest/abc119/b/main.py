N = int(input())
ans = 0
for _ in range(N):
    a, b = input().split()
    if b == "JPY":
        ans += float(a)
    else:
        ans += float(a) * 380000
print(ans)
