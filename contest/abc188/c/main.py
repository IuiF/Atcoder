n = int(input())
a = list(map(int, input().split()))
t = min(max(a[: len(a) // 2]), max(a[len(a) // 2 :]))
print(a.index(t) + 1)
