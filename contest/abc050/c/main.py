from collections import Counter


n = int(input())
a = list(map(int, input().split()))
b = Counter(a)
ans = 1
for i in range(n - 1, -1, -2):
    if b[i] == 2:
        ans *= 2
        ans %= 1000000007
        continue
    elif i == 0 and b[i] == 1:
        break
    else:
        print(0)
        exit()
print(ans)
