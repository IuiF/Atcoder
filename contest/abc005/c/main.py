t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
flag = [False for _ in range(n)]

for i in range(m):
    p = False
    for j in range(n):
        if flag[j] == False and (a[j] <= b[i] <= a[j] + t):
            flag[j] = True
            p = True
            break
        else:
            continue
    if not p:
        print("no")
        exit()
print("yes")
