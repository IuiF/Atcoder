N = int(input())
ans = 0
for i in range(N):
    ans += 1
    if 2**ans > N:
        ans -= 1
        break
print(ans)
