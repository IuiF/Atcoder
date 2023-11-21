n = int(input())
n %= 30
pos = 0
ans = [1, 2, 3, 4, 5, 6]
for _ in range(n):
    ans[pos], ans[pos + 1] = ans[pos + 1], ans[pos]
    pos = (pos + 1) % 5

print(*ans, sep="")
