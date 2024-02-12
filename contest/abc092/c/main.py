n = int(input())
a = list(map(int, input().split()))

total = abs(a[0])
p = a[0]
for i in a[1:]:
    total += abs(p - i)
    p = i
total += abs(p)

a.append(0)
p = 0
for i in range(n):
    if p <= a[i] <= a[i + 1] or p >= a[i] >= a[i + 1]:
        print(total)
    else:
        print(
            total - (max(abs(a[i + 1] - a[i]), abs(p - a[i])) - abs(p - a[i + 1])) * 2
        )
    p = a[i]
