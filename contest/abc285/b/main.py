n = int(input())
s = list(input())

for i in range(1, n):
    ans = 0
    for j in range(0, n - i):
        if s[j] != s[j + i]:
            ans += 1
        else:
            break
    print(ans)
