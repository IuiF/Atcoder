N, M = map(int, input().split())
favs = []

for i in range(N):
    tmp = tuple(list(map(int, input().split())))
    favs.append(set(tmp[1:]))

favs = set.intersection(*favs)

print(len(favs))
