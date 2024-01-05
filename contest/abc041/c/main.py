n = int(input())
a = list(map(int, input().split()))
b = [(a[i], i + 1) for i in range(n)]
b.sort(key=lambda x: x[0], reverse=True)
for i in b:
    print(i[1])
