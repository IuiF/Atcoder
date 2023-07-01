N = int(input())
ans = []


for i in range(1, N + 1):
    a, b = map(int, input().split())
    success_rate = a * 10**30 // (a + b)
    ans.append((success_rate, i))

ans.sort(key=lambda x: (-x[0], x[1]))

print(*[i[1] for i in ans])
