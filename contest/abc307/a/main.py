N = int(input())
Nums = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.append(sum(Nums[7 * i : 7 * i + 7]))
print(*ans)
