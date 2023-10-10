n = int(input())
ans = float("inf")
for i in range(1, 1001):
    for j in range(1, 1001):
        if n >= i * j:
            tmp = n - i * j
            tmp += abs(i - j)
            ans = min(ans, tmp)
        else:
            break
print(ans)
