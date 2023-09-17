a, b, c, d = map(int, input().split())
check = [False for _ in range(101)]
for i in range(1, 101):
    if a < i <= b and c < i <= d:
        check[i] = True
print(sum(check) if sum(check) > 0 else 0)
