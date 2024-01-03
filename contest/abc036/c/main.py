n = int(input())
a = [(int(input()), _) for _ in range(n)]
b = list(set([i[0] for i in a]))
b.sort()
c = {b[i]: i for i in range(len(b))}

for i in a:
    print(c[i[0]])
