import bisect

n, q = map(int, input().split())
r = list(map(int, input().split()))
r.sort()
c_r = [r[0]]
for i in range(1, len(r)):
    c_r.append(r[i] + c_r[-1])

for _ in range(q):
    t = int(input())
    index = bisect.bisect_right(c_r, t)
    print(index)
