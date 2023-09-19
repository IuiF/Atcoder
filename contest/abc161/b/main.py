n, m = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)
ans = 0
for i in A:
    if i >= s / (4 * m):
        ans += 1
print("Yes" if ans >= m else "No")
