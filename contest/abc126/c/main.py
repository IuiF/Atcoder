n, k = map(int, input().split())
ans = 0

for i in range(1, n + 1):
    for j in range(50):
        if i * (2**j) >= k:
            ans += 1 / (2**j)

ans /= 2 * n

print(ans)
