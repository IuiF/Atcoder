from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))
dic = defaultdict(int)

for i in a:
    if i % 4 == 0:
        dic[4] += 1
    elif i % 2 == 0:
        dic[2] += 1
    else:
        dic[1] += 1


if dic[4] >= dic[1]:
    print("Yes")
elif dic[2] == 0 and dic[4] == dic[1] - 1:
    print("Yes")
else:
    print("No")
