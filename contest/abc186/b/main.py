h, w = map(int, input().split())
s = 0
m = 10**10
for _ in range(h):
    a = list(map(int, input().split()))
    s += sum(a)
    m = min(m, min(a))
print(s - m * h * w)
