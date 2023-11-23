n = int(input())
a = sum(i * j for i in range(1, 10) for j in range(1, 10))
ans = []
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == a - n:
            ans.append((i, "x", j))
ans.sort()

for i in ans:
    print(*i)
