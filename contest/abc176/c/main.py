n = int(input())
a = list(map(int, input().split()))
p = 0
ans = 0

for i in a:
    if i >= p:
        p = i
    else:
        ans += p - i
print(ans)
