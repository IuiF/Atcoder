from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))
ans = 0
dic = defaultdict(list)

for i in range(n):
    len_ai = len(dic[a[i]])
    for j in dic[a[i]]:
        ans += i - j - len_ai
        len_ai -= 1

    dic[a[i]].append(i)


print(ans)
