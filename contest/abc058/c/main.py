import collections


N = int(input().rstrip())
ans = None
x = ""

for _ in range(N):
    tmp = list(input().rstrip())
    tmp_d = collections.Counter(tmp)

    if ans is None:
        ans = tmp_d
    else:
        for k, v in ans.items():
            ans[k] = min(ans[k], v, tmp_d.get(k, 0))

for k, v in ans.items():
    x += k * v

x = sorted(x)

print(*x, sep="")
