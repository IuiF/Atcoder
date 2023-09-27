n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append((i + 1, a[i]))
b.sort(key=lambda x: x[1])
print(b[-2][0])
