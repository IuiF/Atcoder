n = int(input())
ans = 1
tmp = 0

while True:
    tmp += ans
    if tmp >= n:
        break
    ans += 1
print(ans)
