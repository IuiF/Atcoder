n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append((a[i], i + 1))
b.sort(key=lambda x: x[0])
print(*[i[1] for i in b])
