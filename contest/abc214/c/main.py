n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

ans = [float("inf")] * n
ans[0] = t[0]

for i in range(1, n):
    tmp = min(ans[i - 1] + s[i - 1], t[i])
    ans[i] = tmp
for i in range(n):
    tmp = min(ans[i - 1] + s[i - 1], t[i])
    ans[i] = tmp

print(*ans, sep="\n")
