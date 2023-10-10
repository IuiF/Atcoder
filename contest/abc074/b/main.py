ans = 0
n = int(input())
k = int(input())
a = list(map(int, input().split()))
for i in a:
    if abs(i) < abs(k - i):
        ans += i * 2
    else:
        ans += abs(k - i) * 2
print(ans)
