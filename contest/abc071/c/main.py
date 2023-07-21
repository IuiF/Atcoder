from collections import defaultdict


N = int(input())
dic = defaultdict(int)
A = list(map(int, input().split()))

for i in A:
    dic[i] += 1

dic = sorted(dic.items(), key=lambda x: x[0], reverse=True)

tmp = 0
for k, v in dic:
    if v >= 4 and not tmp:
        print(k**2)
        exit()
    elif v >= 2 and not tmp:
        tmp = k
    elif v >= 2:
        print(k * tmp)
        exit()

print(0)
