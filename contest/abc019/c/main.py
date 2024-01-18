n = int(input())
a = list(map(int, input().split()))
ans = set()
for i in a:
    while i % 2 == 0:
        i //= 2
    ans.add(i)

print(len(ans))
