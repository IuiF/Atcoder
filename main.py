n = int(input())
topics = list(input().split())
G = [[] for _ in range(n)]

for _ in range(n - 1):
    p, c = map(lambda x: int(x) - 1, input().split())
    G[c] = G[p] + [p]

q = int(input())
for _ in range(q):
    s = list(map(lambda x: int(x) - 1, input().split()))
    t = list(map(lambda x: int(x) - 1, input().split()))

    ans = False
    for t_s in s:
        for t_t in t:
            if t_t == t_s or t_s in G[t_t]:
                ans = True
                break
        if ans:
            break

    print("Yes" if ans else "No")
