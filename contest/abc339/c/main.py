n = int(input())
a = list(map(int, input().split()))
m = 0
l = 0
for i in a:
    m += i
    l = min(l, m)

print(sum(a) - l)
