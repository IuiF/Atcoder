n, t = map(int, input().split())
p = [0, 0]
ans = 0

for _ in range(n):
    a = int(input())
    if p[0] <= a <= p[1]:
        p[1] = a + t
    else:
        ans += p[1] - p[0]
        p[0] = a
        p[1] = a + t
ans += p[1] - p[0]
print(ans)
