n = int(input())
a = list(map(int, input().split()))
if sum(a) / n != sum(a) // n:
    print(-1)
else:
    ans = 0
    ave = sum(a) / n
    pos = 0
    for i in range(1, n + 1):
        if sum(a[pos:i]) / len(a[pos:i]) == ave:
            ans += len(a[pos:i]) - 1
            pos = i
    print(ans)
