N = int(input())
Num = list(map(int, input().split()))[::-1]

for i in range(N - 1):
    tmp = Num[i]
    if Num[i + 1] - Num[i] > 1:
        print("No")
        exit()
    elif Num[i + 1] - Num[i] == 1:
        Num[i + 1] -= 1
print("Yes")
