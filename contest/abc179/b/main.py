n = int(input())
flag = False
tmp = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        tmp += 1
        if tmp == 3:
            flag = True
            if flag:
                break
    else:
        tmp = 0
print("Yes" if flag else "No")
