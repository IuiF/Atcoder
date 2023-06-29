N = int(input())
ans = set()
for _ in range(N):
    tmp = list(input().rsplit())
    for i in tmp:
        ans.add(i)
# ans = sorted(ans)
print(ans, sep="")
