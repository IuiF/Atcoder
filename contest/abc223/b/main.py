s = input() * 2
n = len(s) // 2
arr = []
for i in range(n):
    arr.append(s[i : i + n])
arr.sort()
print(arr[0])
print(arr[-1])
