from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))
dic = defaultdict(int)
t = 0
for i in a:
    if i < 400:
        dic[0] += 1
    elif i < 800:
        dic[1] += 1
    elif i < 1200:
        dic[2] += 1
    elif i < 1600:
        dic[3] += 1
    elif i < 2000:
        dic[4] += 1
    elif i < 2400:
        dic[5] += 1
    elif i < 2800:
        dic[6] += 1
    elif i < 3200:
        dic[7] += 1
    else:
        t += 1

print(max(1, len(dic)), len(dic) + t)
