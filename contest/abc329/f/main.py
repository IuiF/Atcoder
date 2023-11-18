n, q = map(int, input().split())
c = list(map(int, input().split()))
cc = {i: set([c[i - 1]]) for i in range(1, n + 1)}

for _ in range(q):
    a, b = tuple(map(int, input().split()))
    if len(cc[a]) > len(cc[b]):
        cc[a] |= cc[b]
        cc[b] = cc[a]
    else:
        cc[b] |= cc[a]
    cc[a] = set()
    print(len(cc[b]))
