from collections import defaultdict

n, k = map(int, input().split())
c = list(map(int, input().split()))
dic = defaultdict(int)

unique_count = 0
ans = 0

for i in range(k):
    if dic[c[i]] == 0:
        unique_count += 1
    dic[c[i]] += 1
ans = unique_count

for i in range(k, n):
    if dic[c[i - k]] == 1:
        unique_count -= 1
    dic[c[i - k]] -= 1

    if dic[c[i]] == 0:
        unique_count += 1
    dic[c[i]] += 1

    ans = max(ans, unique_count)
    if ans == k:
        break

print(ans)
