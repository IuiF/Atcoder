from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))
dic = defaultdict(int, {i: a[i] for i in range(n)})
default_num = 0

q = int(input())
for _ in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        default_num = que[1]
        dic.clear()
    elif que[0] == 3:
        print(dic[que[1] - 1] + default_num)
    else:
        dic[que[1] - 1] += que[2]
