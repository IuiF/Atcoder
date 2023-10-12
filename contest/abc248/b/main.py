a, b, k = map(int, input().split())
if a >= b:
    print(0)
    exit()
for i in range(10**9):
    a *= k
    if a >= b:
        print(i + 1)
        exit()
