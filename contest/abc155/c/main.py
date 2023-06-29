from collections import Counter


N = int(input())
arr, ans = [], []

for _ in range(N):
    arr.append(input())

arr_d = Counter(arr)
arr = list(arr_d.items())
arr.sort(key=lambda x: x[1])

tmp = arr[-1][1]

while True:
    if len(arr) != 0 and arr[-1][1] == tmp:
        ans.append(arr[-1][0])
        arr.pop()
    else:
        break

print(*sorted(ans), sep="\n")
