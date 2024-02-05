n, k = map(int, input().split())
d = list(input().split())


for i in range(n, 100001):
    flag = True
    for j in list(str(i)):
        if j in d:
            flag = False
            break
    if flag:
        print(i)
        exit()
