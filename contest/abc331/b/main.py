n, s, m, l = map(int, input().split())
ans = float("inf")

for i in range(101):
    for j in range(101):
        for k in range(101):
            if i * 6 + j * 8 + k * 12 >= n:
                t = s * i + m * j + l * k
                ans = min(ans, t)

print(ans)
