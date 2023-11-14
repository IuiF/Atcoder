n, q = map(int, input().split())
s = list(input())
t = 0
for _ in range(q):
    x, y = map(int, input().split())
    if x == 1:
        t -= y
        t %= n
    else:
        tmp = t + y - 1
        tmp %= n
        print(s[tmp])
