n, k = map(int, input().split())
a = list(map(int, input().split()))
a = set(a)
ans = 0
for i in range(k):
    if i in a:
        ans += 1
    else:
        break
print(ans)
