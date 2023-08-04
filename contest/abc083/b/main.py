n, a, b = map(int, input().split())
ans: int = 0


for i in range(n + 1):
    tmp = 0
    i_tmp = i
    for j in range(len(str(i))):
        tmp += i_tmp % 10
        i_tmp //= 10
    if a <= tmp <= b:
        ans += i

print(ans)
