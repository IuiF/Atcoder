n = int(input())
a = list(map(int, input().split()))
ans = [False for _ in range(n)]
for i in range(n):
    if ans[i] == False:
        ans[a[i] - 1] = True
print(ans.count(False))
b = []
for i in range(n):
    if ans[i] == False:
        b.append(i + 1)
print(*b)
