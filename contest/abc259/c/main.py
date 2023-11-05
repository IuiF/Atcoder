s = input()
t = input()

i = 0
a = []
while i < len(s):
    tmp = s[i]
    num = 1
    j = i + 1
    while j < len(s):
        if s[j] != tmp:
            break
        else:
            num += 1
            j += 1
    a.append((tmp, num))
    i = j
i = 0
b = []
while i < len(t):
    tmp = t[i]
    num = 1
    j = i + 1
    while j < len(t):
        if t[j] != tmp:
            break
        else:
            num += 1
            j += 1
    b.append((tmp, num))
    i = j


if len(a) != len(b):
    print("No")
    exit()
for i in range(len(a)):
    if a[i] == b[i]:
        continue
    elif a[i][0] != b[i][0]:
        print("No")
        exit()
    elif a[i][1] == 1:
        print("No")
        exit()
    elif a[i][1] > b[i][1]:
        print("No")
        exit()


print("Yes")
