n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [(i, 0) for i in a]
for i in b:
    c.append((i, 1))  # type: ignore

c.sort(key=lambda x: x[0])

A, B = [], []
for i in range(m + n):
    if c[i][1] == 0:
        A.append(i + 1)
    else:
        B.append(i + 1)

print(*A)
print(*B)
