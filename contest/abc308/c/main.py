from decimal import Decimal, getcontext


N = int(input())
ans = []

getcontext().prec = 26

for i in range(1, N + 1):
    a, b = map(Decimal, input().split())
    success_rate = a / (a + b)
    ans.append((success_rate, i))

ans.sort(key=lambda x: (-x[0], x[1]))

print(*[i[1] for i in ans])
