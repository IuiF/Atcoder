n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = [0 for _ in range(n)]
ans[0] = 1
p = 0
for i in range(1, n):
    if a[i - 1] != a[i]:
        p += 1
        ans[p] += 1
    else:
        ans[p] += 1

print(*ans, sep="\n")
