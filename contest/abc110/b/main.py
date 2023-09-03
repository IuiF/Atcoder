n, m, x, y = map(int, input().split())
X = max(list(map(int, input().split())))
Y = min(list(map(int, input().split())))
arr = [i + 1 for i in range(x, y)]
flag = False
for i in arr:
    if X < i <= Y:
        flag = True
        break
print("No War" if flag else "War")
