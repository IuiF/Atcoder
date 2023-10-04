n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    if i % 6 == 0:
        ans += 3
    elif i % 6 == 5:
        ans += 2
    elif i % 6 == 4 or i % 6 == 2:
        ans += 1
print(ans)
