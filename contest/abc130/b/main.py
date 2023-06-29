n, x = map(int, input().split())
arr = list(map(int, input().split()))
arr_total = [0]
count = 1
for i in range(n):
    arr_total.append(arr[i] + arr_total[i])
    if arr_total[-1] <= x:
        count += 1

print(count)
