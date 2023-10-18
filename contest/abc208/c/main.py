n, k = map(int, input().split())
a = list(map(int, input().split()))
b = set(sorted(a)[: k % n])
for i in a:
    if i in b:
        print(k // n + 1)
    else:
        print(k // n)
