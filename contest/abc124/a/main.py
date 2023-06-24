nums = list(map(int, input().split()))
if nums[0] == nums[1]:
    print(nums[0] * 2)
else:
    print(max(nums) * 2 - 1)
