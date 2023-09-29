a = list(map(int, input().split()))
for _ in range(int(input())):
    a[a.index(max(a))] = max(a) * 2
print(sum(a))
