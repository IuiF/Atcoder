from collections import defaultdict


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


n = int(input())
d = defaultdict(int)
t = 1
ans = 1

for i in range(1, n + 1):
    arr = factorization(i)
    for j, k in arr:
        d[j] += k

for i, j in d.items():
    if i == 1:
        continue
    ans *= j + 1
    ans %= 1000000007

print(ans)
