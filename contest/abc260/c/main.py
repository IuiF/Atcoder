n, x, y = map(int, input().split())
r = 1
if n == 1:
    print(0)
    exit()
ans = x
for _ in range(n - 2):
    r = r + ans
    ans = ans * y + r * x
ans *= y

print(ans)
