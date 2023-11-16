n, k = input().split()
n = list(n)
k = int(k)

for _ in range(k):
    a = "".join(sorted(n, reverse=True))
    b = "".join(sorted(n))
    t = int(a) - int(b)
    n = list(str(t))

print("".join(n))
