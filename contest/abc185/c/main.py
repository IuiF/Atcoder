def ac(n):
    tmp = 1
    for i in range(1, n + 1):
        tmp *= i
    return tmp


L = int(input())
ans = ac(L - 1) // (ac(L - 12) * ac(11))
print(ans)
