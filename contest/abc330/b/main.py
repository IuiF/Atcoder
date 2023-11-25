n, l, r = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for i in a:
    if i < l:
        ans.append(l)
    elif i > r:
        ans.append(r)
    else:
        ans.append(i)
print(*ans)
