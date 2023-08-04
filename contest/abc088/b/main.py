N = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

if N % 2 == 0:
    Ans = sum(nums[i * 2] for i in range(N // 2)) - sum(
        nums[i * 2 + 1] for i in range(N // 2)
    )
else:
    Ans = sum(nums[i * 2] for i in range(N // 2 + 1)) - sum(
        nums[i * 2 + 1] for i in range(N // 2)
    )

print(Ans)
