h = int(input())

n = 0
while True:
    if 2 ** (n) <= h < 2 ** (n + 1):
        break
    n += 1

ans = 0
for i in range(0, n + 1):
    ans += 2 ** (i)

print(ans)
