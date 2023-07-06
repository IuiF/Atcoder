K = int(input())

if K % 2 == 0:
    print(-1)
    exit()

for i in range(1, K):
    tmp = int("7" * i)
    if tmp % K == 0:
        print(i)
        exit()
