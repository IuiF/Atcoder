n, m = map(int, input().split())
a = list(map(int, input().split()))
dic = {i: 0 for i in range(1, n + 1)}
maxi = 1
for i in a:
    dic[i] += 1
    if dic[i] > dic[maxi] or (dic[i] == dic[maxi] and i < maxi):
        maxi = i
    print(maxi)
