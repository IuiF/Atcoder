n = list(input())
ans = 0
for i in range(1, 2 ** len(n)):
    a, b = [], []
    for j in range(len(n)):
        if i & (1 << j):
            a.append(n[j])
        else:
            b.append(n[j])
    if len(a) == 0 or len(b) == 0:
        continue
    a = "".join(sorted(a, reverse=True))
    b = "".join(sorted(b, reverse=True))
    ans = max(ans, int(a) * int(b))
print(ans)
