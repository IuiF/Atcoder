n, s, d = map(int, input().split())
for _ in range(n):
    a, b = map(int, input().split())
    if a >= s or b <= d:
        continue
    else:
        print("Yes")
        exit()
print("No")
