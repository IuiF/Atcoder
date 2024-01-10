def solve(n, arr):
    ans = []
    ans.extend(arr)
    ans.append(n)
    ans.extend(arr)
    return ans


n = int(input())
ans = []
for i in range(1, n + 1):
    ans = solve(i, ans)

print(*ans)
