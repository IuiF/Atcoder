n = int(input())
s = [list(input()) for _ in range(n)]

ans = float("inf")

for i in range(10):
    i = str(i)
    arr = [0 for _ in range(10)]
    for j in s:
        arr[j.index(i)] += 1
    M = max(arr)
    for j in range(9, -1, -1):
        if arr[j] == M:
            t = 10 * (M - 1) + j
            break
    ans = min(ans, t)

print(ans)
