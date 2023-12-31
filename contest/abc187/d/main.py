n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sum_aoki = sum(i[0] for i in arr)
sum_taka = 0
arr.sort(key=lambda x: -(2 * x[0] + x[1]))

for i in range(n):
    sum_aoki -= arr[i][0]
    sum_taka += sum(arr[i])
    if sum_aoki < sum_taka:
        print(i + 1)
        exit()
