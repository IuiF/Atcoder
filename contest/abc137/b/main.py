k, x = map(int, input().split())
nums = list(range(-15000000, 15000000))

print(*nums[(x - k + 15000001) : (x + k + 15000000)])
