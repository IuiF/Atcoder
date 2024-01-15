n = int(input())
a = list(map(int, input().split()))


ans = float("inf")

for i in range(-100, 101):
    t = 0
    for j in a:
        t += (j - i) ** 2
    ans = min(ans, t)

print(ans)
