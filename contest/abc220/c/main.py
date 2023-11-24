n = int(input())
a = list(map(int, input().split()))
s = sum(a)
x = int(input())

ans = (x // s) * n
x %= s

for i in a:
    x -= i
    ans += 1
    if x < 0:
        break

print(ans)
