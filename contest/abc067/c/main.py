n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(1, n):
    b.append(a[i] + b[-1])

ans = 10**10
for i in range(n - 1):
    ans = min(ans, abs(b[-1] - 2 * b[i]))

print(ans)
