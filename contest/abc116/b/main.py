from collections import defaultdict


s = int(input())
dic = defaultdict(int)
dic[s] += 1
i = 2

while True:
    if s % 2 == 0:
        s = s // 2
    else:
        s = s * 3 + 1

    if dic[s] != 0:
        print(i)
        exit()
    else:
        dic[s] += 1

    i += 1
