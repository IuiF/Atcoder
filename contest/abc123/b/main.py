import math

p = [int(input()) for _ in range(5)]
q = [i % 10 for i in p]
r = [math.ceil(i / 10) * 10 for i in p]
q.sort()
t = 0
for i in q:
    if i == 0:
        continue
    else:
        t = i
        break
print(sum(r) + t if sum(q) == 0 else sum(r) + t - 10)
