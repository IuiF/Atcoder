n, q = map(int, input().split())
s = list(input())
arr = [0]
for i in range(1, n):
    if s[i - 1] == s[i]:
        t = arr[-1] + 1
        arr.append(t)
    else:
        arr.append(arr[-1])

for _ in range(q):
    l, r = map(int, input().split())
    print(arr[r - 1] - arr[l - 1])
