import math


n = int(input())
p = list(map(int, input().split()))
a = [(p[i], i) for i in range(n)]
a.sort(reverse=True, key=lambda x: x[0])

ans = -float("inf")
contests = []

for perf, index in a:
    contests.append((perf, index))
    contests = sorted(contests, key=lambda x: x[1])

    sum_p = 0
    sum_w = 0
    for k, (p, _) in enumerate(contests):
        weight = 0.9 ** (len(contests) - k - 1)
        sum_p += weight * p
        sum_w += weight
    rate = sum_p / sum_w - (1200 / math.sqrt(len(contests)))
    if rate > ans:
        ans = rate
    else:
        contests = contests[:-1]

print(ans)
