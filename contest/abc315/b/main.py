M = int(input())
D = list(map(int, input().split()))
sum = (sum(D) + 1) // 2

for i in range(len(D)):
    if sum <= D[i]:
        print(i + 1, sum)
        exit()
    else:
        sum -= D[i]
