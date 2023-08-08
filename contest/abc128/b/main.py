n = int(input())
book = []
for i in range(n):
    a, b = input().split()
    book.append([a, int(b), i + 1])
book.sort(key=lambda x: (x[0], -x[1]))

print(*[x[2] for x in book], sep="\n")
