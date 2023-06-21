k, x = map(int, input().split())
nums = list(range(-150, 150))

print(*nums[(x - k + 151) : (x + k + 150)])
