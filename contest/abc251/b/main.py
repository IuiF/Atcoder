n, w = map(int, input().split())
a = list(map(int, input().split()))
ans = set()
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            if i == j == k:
                if a[i] <= w:
                    ans.add(a[i])
            elif i == j != k:
                if a[i] + a[k] <= w:
                    ans.add(a[i] + a[k])
            elif i != j == k:
                if a[i] + a[k] <= w:
                    ans.add(a[i] + a[k])
            elif i != j != k:
                if a[i] + a[j] + a[k] <= w:
                    ans.add(a[i] + a[j] + a[k])
print(len(ans))
