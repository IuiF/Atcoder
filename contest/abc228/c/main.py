n, k = map(int, input().split())
p = [sum(map(int, input().split())) for _ in range(n)]
q = sorted(p, reverse=True)
t = q[k - 1]

for i in p:
    if t - i - 300 <= 0:
        print("Yes")
    else:
        print("No")
