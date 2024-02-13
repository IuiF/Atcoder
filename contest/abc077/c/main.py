n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

p_a = 0
p_c = 0

ans = 0
for i in b:
    while p_a < n and a[p_a] < i:
        p_a += 1
    while p_c < n and c[p_c] <= i:
        p_c += 1
    ans += (p_a) * (n - p_c)

print(ans)
