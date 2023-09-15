n = int(input())
a = list(map(int, input().split()))
ans = 1
if 0 in set(a):
    ans = 0

for i in a:
    ans *= i
    if ans > (10**18):
        print(-1)
        exit()

print(ans)
