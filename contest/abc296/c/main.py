n, x = map(int, input().split())
x = abs(x)
a = list(set(list(map(int, input().split()))))
a.sort()
i = 0
j = 0
flag = False

while i < len(a):
    while j < len(a):
        if x == a[j] - a[i]:
            flag = True
            break
        elif x > a[j] - a[i]:
            j += 1
            continue
        else:
            break
    i += 1
    if flag:
        break


print("Yes" if flag else "No")
