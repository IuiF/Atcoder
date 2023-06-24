n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(1, n - 1):
    if max(p[i - 1 : i + 2]) != p[i] and min(p[i - 1 : i + 2]) != p[i]:
        ans += 1
print(ans)
