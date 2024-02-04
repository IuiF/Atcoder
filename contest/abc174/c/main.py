K = int(input())

ans = -1
n = 7
for i in range(K):
    if n % K == 0:
        ans = i + 1
        break
    else:
        n %= K
        n = n * 10 + 7

print(ans)
