n, m = map(int, input().split())
friends = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(n):
    ans = set()
    for j in friends[i]:
        for k in friends[j]:
            ans.add(k)
    ans.discard(i)
    for j in friends[i]:
        ans.discard(j)

    print(len(ans))
