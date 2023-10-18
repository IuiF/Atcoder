n = int(input())
arr = []
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == 1:
        arr.append((b, c))
    elif a == 2:
        arr.append((b, c - 0.1))
    elif a == 3:
        arr.append((b + 0.1, c))
    else:
        arr.append((b + 0.1, c - 0.1))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if min(arr[i][1], arr[j][1]) - max(arr[i][0], arr[j][0]) >= 0:
            ans += 1

print(ans)
