from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

G = defaultdict(list)
color = {}

for i in range(m):
    G[a[i]].append(b[i])
    G[b[i]].append(a[i])

flag = True

s = []
for i in G:
    if i not in color:
        color[i] = 0
        s.append((i, None))

        while s:
            now, pn = s.pop()
            for j in G[now]:
                if j == pn:
                    continue
                if j in color:
                    if color[j] == color[now]:
                        flag = False
                        break
                else:
                    color[j] = 1 - color[now]
                    s.append((j, now))

        if not flag:
            break

print("Yes" if flag else "No")
