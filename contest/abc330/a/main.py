n, l = map(int, input().split())
a = list(map(int, input().split()))
ans = sum(1 for i in a if i >= l)
print(ans)
