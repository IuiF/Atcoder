n = int(input())
x = list(map(int, input().split()))
y = sorted(x)
i = y[n // 2 - 1]
j = y[n // 2]

for t in x:
    if i < t:
        print(i)
    else:
        print(j)
