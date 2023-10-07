import bisect

n = int(input())
d = {}
for i in range(n):
    s, c = map(int, input().split())
    d[s] = c
d = sorted(d.items())
ans = 0

for i, j in d:
    if j > 1:
        new_s = 2 * i
        add_c = j // 2
        rem_c = j % 2
        ans += rem_c

        idx = bisect.bisect_right(d, (new_s, 0))
        if idx < len(d) and d[idx][0] == new_s:
            d[idx] = (new_s, d[idx][1] + add_c)
        else:
            d.insert(idx, (new_s, add_c))
    else:
        ans += j

print(ans)
