n, k = map(int, input().split())
s = list(input() for _ in range(k))
s.sort()
for i in s:
    print(i)
