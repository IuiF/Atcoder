n, k = map(int, input().split())
ans = k
for _ in range(1, n):
    ans *= k - 1
print(ans)
