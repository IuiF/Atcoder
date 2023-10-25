n = int(input())
ans = float("inf")
for i in range(1, int(n ** (1 / 2)) + 1):
    if n % i == 0:
        j = n // i
        ans = min(ans, j + i - 2)

print(ans)
