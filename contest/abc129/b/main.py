n = int(input())
w = [int(x) for x in input().split()]
ans = 10 * 10


for i in range(2, 101):
    a = sum(w[:i])
    b = sum(w[i:])
    ans = min(ans, abs(a - b))


print(ans)
