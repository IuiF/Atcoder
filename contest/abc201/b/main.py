N = int(input())
arr = []
for _ in range(N):
    tmp = list(input().split())
    arr.append([tmp[0], int(tmp[1])])
arr.sort(reverse=True, key=lambda arr: arr[1])

print(arr[1][0])
