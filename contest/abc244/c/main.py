n = int(input())
dic = {i: False for i in range(1, 2 * n + 2)}
pos = 1
t = False

while sum(dic.values()) < 2 * n + 1:
    if dic[pos] == False:
        print(pos)
        dic[pos] = True
        t = True
    pos += 1

    if t == True:
        q = int(input())
        dic[q] = True
        t = False
