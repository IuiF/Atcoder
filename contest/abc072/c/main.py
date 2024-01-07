from collections import defaultdict


n = int(input())
dic = defaultdict(int)
a = list(map(int, input().split()))
for i in a:
    dic[i] += 1
    dic[i + 1] += 1
    dic[i - 1] += 1

print(max(dic.values()))
