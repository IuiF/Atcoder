n = int(input())
for i in range(998244353):
    if (n - i) % 998244353 == 0:
        print(i)
        exit()
